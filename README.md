# ライフサイエンス研究者のためのAIエージェントチュートリアル

研究データベースを効率的に活用し、レベルに応じたAIエージェント活用法を学ぶチュートリアルです。

## 🎯 プロジェクトの目的

このプロジェクトは、コードを書くのが必ずしも得意ではないライフサイエンス研究者が、それぞれのレベルに応じた方法で自身の研究にAIエージェントを活用できるようになることを目的としています。PubMed、UniProt、ChEMBLなどの研究データベースを、SQLクエリやAPIリクエストなしで効率的に活用する方法を学びます。

## 📚 ドキュメント

ドキュメントはMkDocsで管理され、GitHub Pagesで公開されています。

- [オンラインドキュメント](https://fuku-inc.github.io/life-science-agent-tutorial/)

## 🚀 クイックスタート

### ローカルでドキュメントを確認

```bash
# 依存関係のインストール
pip install -r requirements-docs.txt

# ドキュメントサーバーの起動
mkdocs serve

# ブラウザで http://localhost:8000 を開く
```

### ドキュメントのビルド

```bash
mkdocs build
```

## 📖 チュートリアル構成

### レベル1：既存のAIエージェントサービスの利用
コードを書かずに、すぐに使えるAIエージェントサービスを活用します。

- **Manus** - コンピュータを自動操作するAIエージェント
- **Operator** - ブラウザを自動操作するAIエージェント
- **ChatGPT** - OpenAIの対話型AIエージェント

### レベル2：MCPを利用したツールの追加
Model Context Protocol (MCP) を使って、研究に特化したツールを追加します。

- **Claude Desktop** - ライフサイエンスDBアクセスツールの設定
- **ChatGPT Custom** - カスタムアクションでDB検索を実現

### レベル3：フレームワークを利用したエージェントシステムの構築
研究ワークフローに合わせたエージェントシステムを構築します。

- **ADK (Agent Development Kit)** - シンプルなエージェント開発
- **AutoGen** - 対話型エージェントの構築

### レベル4：マルチエージェントシステム
複数のエージェントを組み合わせて、複雑な研究タスクを自動化します。（準備中）

## 🔗 リソース

### ベンチマーク
- [SWE-bench](https://www.swebench.com/) - ソフトウェアエンジニアリングタスクのベンチマーク
- [WebArena](https://webarena.dev/) - Webベースのタスク自動化ベンチマーク
- [GAIA](https://huggingface.co/gaia-benchmark) - 汎用AIアシスタントのベンチマーク

### 学習資料
- [The Landscape of Emerging AI Agent Architectures](https://www.deeplearning.ai/the-batch/the-landscape-of-emerging-ai-agent-architectures-for-reasoning-planning-and-tool-calling-a-survey/) - AIエージェントアーキテクチャの概観
- [Model Context Protocol](https://modelcontextprotocol.io/) - MCPの公式ドキュメント
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) - エージェント構築フレームワーク

## 🤝 コントリビューション

コントリビューションを歓迎します！詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## 📝 ライセンス

このプロジェクトは [Creative Commons Attribution 4.0 International License (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) の下で公開されています。

これは以下のことを意味します：
- ✅ **自由に共有** - どのような媒体や形式でもコピー、再配布が可能
- ✅ **自由に翻案** - リミックス、変更、別の作品のベースとして利用が可能  
- ✅ **商用利用可能** - 営利目的での利用も可能
- ⚠️ **帰属表示が必要** - 適切なクレジット表示とライセンスへのリンクが必要

### 帰属表示の例

このチュートリアルを利用する際は、以下のような帰属表示をお願いします：

```
本資料は「ライフサイエンス研究者のためのAIエージェントチュートリアル」
https://github.com/fuku-inc/life-science-agent-tutorial
を基に作成されました。CC BY 4.0ライセンスの下で利用しています。
```