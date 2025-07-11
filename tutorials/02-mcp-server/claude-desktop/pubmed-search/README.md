# PubMed MCP サーバー

Claude Desktop用のPubMed検索機能を提供するModel Context Protocol (MCP)サーバーです。

## クイックスタート

1. **Dockerイメージのビルド**:
   ```bash
   docker build -t pubmed-mcp-server .
   ```

2. **Claude Desktopの設定**:
   `claude_desktop_config.json`の`mcpServers`セクションに以下を追加します：
   
   **注意**: すでに他のMCPサーバーが設定されている場合は、既存の設定を削除せずに`pubmed`の設定を追加してください。
   
   ```json
   {
     "mcpServers": {
       // 既存のサーバー設定はそのまま残す
       "pubmed": {
         "command": "docker",
         "args": [
           "run",
           "-i",
           "--rm",
           "pubmed-mcp-server"
         ],
         "env": {}
       }
     }
   }
   ```

3. **Claude Desktopを再起動**して設定を反映させます。

## 利用可能なツール

- **search_pubmed**: PubMedで科学論文を検索
  - パラメータ:
    - `query` (必須): 検索キーワード
    - `max_results`: 最大結果数 (デフォルト: 10)
    - `sort`: 'relevance'（関連性）または'date'（日付）でソート (デフォルト: 'relevance')
    - `date_from`: 開始日 (YYYY/MM/DD形式)
    - `date_to`: 終了日 (YYYY/MM/DD形式)

- **get_article_details**: 特定の論文の詳細情報を取得
  - パラメータ:
    - `pmid` (必須): 論文のPubMed ID

## 使用例

Claude Desktopで以下のようなコマンドが使えます：

- 「2023年のCOVID-19ワクチンに関する論文をPubMedで検索して」
- 「山中伸弥の論文を探して」
- 「PMID 12345678の詳細を取得して」

## トラブルシューティング

Dockerイメージを手動でテスト:
```bash
docker run -it --rm pubmed-mcp-server
```
(Ctrl+Cで終了)

イメージがビルドされているか確認:
```bash
docker images | grep pubmed-mcp-server
```

必要に応じてイメージを再ビルド:
```bash
docker build -t pubmed-mcp-server . --no-cache
```