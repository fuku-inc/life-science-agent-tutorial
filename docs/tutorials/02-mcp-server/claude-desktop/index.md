# Claude Desktop

## 概要

Claude Desktopは、AIアシスタントのClaudeをデスクトップアプリケーションとして利用できるツールです。Model Context Protocol（MCP）を通じて、外部ツールと連携することで、研究データベースへのアクセスや論文検索などの作業を効率化できます。

このページでは、Claude DesktopとMCPの基本的な仕組みを理解し、研究活動での活用方法を学びます。

## 学習目標

このチュートリアルを完了すると、以下のことができるようになります：

- 🛠️ **Claude Desktopのセットアップ** を行い、基本的な操作ができる
- 🔧 **MCPツールの追加と設定** ができ、研究に必要なツールを導入できる


## Claude Desktopのセットアップ

### インストール手順

Claude Desktopのインストール方法については、[インストールガイド](../../../getting-started/installation/claude-desktop.md)を参照してください。


### 初期設定

1. Claude Desktopを起動
2. Anthropicアカウントでログイン（アカウントがない場合は新規作成）
3. 利用規約に同意
4. 基本的な設定（テーマ、フォントサイズなど）を調整

## MCPツールの追加方法

### 設定ファイルの場所

MCPツールの設定は、`claude_desktop_config.json`ファイルで管理されます。

#### ファイルの場所

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

### 設定ファイルの基本構造

```json
{
  "mcpServers": {
    "ツール名": {
      "command": "実行コマンド",
      "args": ["引数1", "引数2"],
      "env": {
        "環境変数名": "値"
      }
    }
  }
}
```

### ツール追加の手順

1. Claude Desktopを終了
2. 設定ファイルを開く（存在しない場合は新規作成）
3. ツールの設定を追加
4. ファイルを保存
5. Claude Desktopを再起動

## 利用シーン別チュートリアル

研究活動での具体的な活用方法を、シナリオ別に学習できます：

### 📚 [PubMedを使った文献検索](pubmed-search.md)
MCPツールを使ってPubMedから効率的に論文を検索し、結果を整理する方法を学びます。

## 次のステップ

Claude Desktop + MCPの基本を理解したら、以下のステップに進むことをお勧めします：

1. **実践的な活用**: 各利用シーンのチュートリアルを試す
2. **カスタマイズ**: 自分の研究分野に特化したツールを追加
3. **高度な活用**: レベル3（エージェント構築）へ進む

---

### **関連リンク**:

- [レベル2のトップページに戻る](../index.md)
- [他のチュートリアルを見る](../../index.md#チュートリアル一覧)