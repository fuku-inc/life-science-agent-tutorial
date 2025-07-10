# Claude Desktop セットアップガイド

Claude Desktopは、Anthropic社のAIアシスタントClaudeをデスクトップアプリケーションとして利用できるツールです。MCPサーバーと連携することで、ローカルファイルへのアクセスなど拡張機能を利用できます。

## 前提条件

- Anthropicアカウント（無料プランでも可）
- OS
    - macOS: macOS 11 (Big Sur) 以上
    - Windows: Windows 10 以上

## Claude Desktopのインストール

### ダウンロード

1. [Claude Desktop](https://claude.ai/download)の公式ページにアクセス
2. お使いのOSに対応したバージョンをダウンロード：
    - macOS: `.dmg` ディスクイメージ
    - Windows: `.exe` インストーラー
    - Linux: **現在Linux版は提供されていません** 

### インストール手順

#### Windows

1. ダウンロードした `.exe` ファイルを実行
2. インストールウィザードの指示に従う
3. デフォルト設定のままで問題ありません

#### macOS

1. ダウンロードした `.dmg` ファイルを開く
2. Claude.app を Applications フォルダにドラッグ
3. 初回起動時に「開発元が未確認」と表示された場合：
   - システム環境設定 → セキュリティとプライバシー → 「このまま開く」


## サポート情報

問題が発生した場合は、以下の公式ドキュメントを参照してください：

- [Claude for Desktopのインストール](https://support.anthropic.com/ja/articles/10065433) - インストールや基本的な使い方


---

### **関連リンク**:

- [インストールガイドに戻る](index.md)
- [Docker環境のセットアップ](docker.md)
- [レベル2チュートリアル](../../tutorials/02-mcp-server/index.md)