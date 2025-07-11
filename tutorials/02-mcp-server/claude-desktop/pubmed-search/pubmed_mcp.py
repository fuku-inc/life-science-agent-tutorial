"""PubMed MCP サーバー

PubMed検索機能へのアクセスを提供するModel Context Protocolサーバー。
このサーバーにより、Claude DesktopからMCPツールを通じて直接PubMedを検索できます。
"""

import logging
from typing import Any, Dict, List, Optional
from urllib.parse import quote
import httpx
import xml.etree.ElementTree as ET

from mcp.server.fastmcp import FastMCP

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# PubMed APIの設定
PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
PUBMED_SEARCH_URL = f"{PUBMED_BASE_URL}/esearch.fcgi"
PUBMED_FETCH_URL = f"{PUBMED_BASE_URL}/efetch.fcgi"

# MCPサーバーインスタンスの作成
server = FastMCP("pubmed-mcp")


async def search_pubmed_api(
    query: str,
    max_results: int = 10,
    sort: str = "relevance",
    date_from: Optional[str] = None,
    date_to: Optional[str] = None
) -> List[str]:
    """PubMedを検索してPMIDのリストを返す"""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "sort": sort
    }
    
    # 日付フィルターを追加（指定された場合）
    if date_from:
        params["mindate"] = date_from
    if date_to:
        params["maxdate"] = date_to
    
    async with httpx.AsyncClient() as client:
        response = await client.get(PUBMED_SEARCH_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        pmid_list = data.get("esearchresult", {}).get("idlist", [])
        
        return pmid_list


async def fetch_article_details(pmids: List[str]) -> List[Dict[str, Any]]:
    """指定されたPMIDの詳細情報を取得"""
    if not pmids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(PUBMED_FETCH_URL, params=params)
        response.raise_for_status()
        
        # XMLレスポンスをパース
        root = ET.fromstring(response.text)
        articles = []
        
        for article in root.findall(".//PubmedArticle"):
            try:
                # 論文情報を抽出
                medline = article.find(".//MedlineCitation")
                pmid = medline.find(".//PMID").text
                
                # タイトル
                title_elem = medline.find(".//ArticleTitle")
                title = title_elem.text if title_elem is not None else "タイトルなし"
                
                # 著者
                authors = []
                for author in medline.findall(".//Author"):
                    last_name = author.find(".//LastName")
                    fore_name = author.find(".//ForeName")
                    if last_name is not None and fore_name is not None:
                        authors.append(f"{last_name.text} {fore_name.text}")
                
                # 要約
                abstract_elem = medline.find(".//AbstractText")
                abstract = abstract_elem.text if abstract_elem is not None else "要約はありません"
                
                # 雑誌情報
                journal = medline.find(".//Journal")
                journal_title = journal.find(".//Title").text if journal is not None else "不明"
                
                # 出版日
                pub_date = medline.find(".//PubDate")
                year = pub_date.find(".//Year")
                year_text = year.text if year is not None else "不明"
                
                articles.append({
                    "pmid": pmid,
                    "title": title,
                    "authors": authors,
                    "journal": journal_title,
                    "year": year_text,
                    "abstract": abstract
                })
                
            except Exception as e:
                logger.error(f"Error parsing article {pmid}: {str(e)}")
                continue
        
        return articles


@server.tool()
async def search_pubmed(
    query: str,
    max_results: int = 10,
    sort: str = "relevance",
    date_from: Optional[str] = None,
    date_to: Optional[str] = None
) -> str:
    """PubMedで科学論文を検索
    
    Args:
        query: 検索クエリ（キーワード、著者名など）
        max_results: 返す結果の最大数（デフォルト: 10）
        sort: ソート順 - 'relevance'（関連性）または 'date'（日付）（デフォルト: 'relevance'）
        date_from: 検索開始日（YYYY/MM/DD形式）
        date_to: 検索終了日（YYYY/MM/DD形式）
    
    Returns:
        検索結果のフォーマットされた文字列
    """
    try:
        # PubMedを検索
        pmids = await search_pubmed_api(query, max_results, sort, date_from, date_to)
        
        if not pmids:
            return "検索クエリに該当する結果が見つかりませんでした。"
        
        # 論文の詳細を取得
        articles = await fetch_article_details(pmids)
        
        # 結果をフォーマット
        results = []
        for i, article in enumerate(articles, 1):
            result = f"""
**{i}. {article['title']}**
- **著者**: {', '.join(article['authors'][:5])}{'...' if len(article['authors']) > 5 else ''}
- **雑誌**: {article['journal']} ({article['year']})
- **PMID**: {article['pmid']}
- **要約**: {article['abstract'][:500]}{'...' if len(article['abstract']) > 500 else ''}
"""
            results.append(result)
        
        return f"{len(articles)}件の論文が見つかりました：\n\n" + "\n---\n".join(results)
        
    except Exception as e:
        logger.error(f"Error searching PubMed: {str(e)}")
        return f"PubMed検索エラー: {str(e)}"


@server.tool()
async def get_article_details(pmid: str) -> str:
    """PMIDを指定してPubMed論文の詳細情報を取得
    
    Args:
        pmid: 論文のPubMed ID
    
    Returns:
        論文の詳細情報のフォーマットされた文字列
    """
    try:
        articles = await fetch_article_details([pmid])
        
        if not articles:
            return f"PMID: {pmid} の論文が見つかりませんでした"
        
        article = articles[0]
        result = f"""
**タイトル**: {article['title']}

**著者**: {', '.join(article['authors'])}

**雑誌**: {article['journal']} ({article['year']})

**PMID**: {article['pmid']}

**要約**: {article['abstract']}
"""
        
        return result
        
    except Exception as e:
        logger.error(f"Error fetching article details: {str(e)}")
        return f"論文詳細取得エラー: {str(e)}"


async def main():
    """MCPサーバーのメインエントリポイント"""
    # FastMCP 1.0の標準的な起動方法
    from mcp.server import Server
    from mcp.server.models import InitializationOptions
    import mcp.types as types
    
    # 低レベルのServerインスタンスを作成
    mcp_server = Server("pubmed-mcp")
    
    # ツールを登録
    @mcp_server.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="search_pubmed",
                description="PubMedで科学論文を検索",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "検索クエリ"},
                        "max_results": {"type": "integer", "default": 10},
                        "sort": {"type": "string", "enum": ["relevance", "date"], "default": "relevance"},
                        "date_from": {"type": "string", "pattern": "^\\d{4}/\\d{2}/\\d{2}$"},
                        "date_to": {"type": "string", "pattern": "^\\d{4}/\\d{2}/\\d{2}$"}
                    },
                    "required": ["query"]
                }
            ),
            types.Tool(
                name="get_article_details",
                description="PMIDを指定してPubMed論文の詳細情報を取得",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "pmid": {"type": "string", "description": "論文のPubMed ID"}
                    },
                    "required": ["pmid"]
                }
            )
        ]
    
    @mcp_server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        if name == "search_pubmed":
            result = await search_pubmed(**arguments)
        elif name == "get_article_details":
            result = await get_article_details(**arguments)
        else:
            result = f"Unknown tool: {name}"
        
        return [types.TextContent(type="text", text=result)]
    
    async with stdio_server() as (read_stream, write_stream):
        await mcp_server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="pubmed-mcp",
                server_version="1.0.0"
            )
        )


if __name__ == "__main__":
    import sys
    
    # SSEトランスポートのサポートを追加
    if len(sys.argv) > 1 and sys.argv[1] == "--sse":
        # ポート番号を引数から取得（デフォルト: 8080）
        port = 8080
        if len(sys.argv) > 2:
            try:
                port = int(sys.argv[2])
            except ValueError:
                print(f"Invalid port number: {sys.argv[2]}, using default port {port}")
        
        # SSEモードで実行
        print(f"Starting PubMed MCP server in SSE mode on port {port}...")
        server.run(transport="sse", port=port)
    else:
        # STDIOモードで実行（デフォルト）
        server.run(transport="stdio")