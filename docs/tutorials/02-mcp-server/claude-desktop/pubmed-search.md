# PubMed検索チュートリアル

## 概要

このチュートリアルでは、Claude Desktop + MCPを使用してPubMed（医学・生物学分野の論文データベース）を効率的に検索する方法を学びます。Python製のMCPサーバーをDockerで実行し、Claude Desktopから直接PubMed検索を行えるようにします。

## 学習目標

このチュートリアルを完了すると、以下のことができるようになります：

- 🔧 **PubMed MCPサーバーのセットアップ** ができる
- 🔍 **効率的な文献検索** をClaude Desktopから直接実行できる
- 📊 **検索結果の整理と分析** をAIアシスタントに任せられる
- 🚀 **研究ワークフローの自動化** への第一歩を踏み出せる

## 前提条件

- Claude Desktopがインストール済み（[Claude Desktop セットアップガイド](../../../getting-started/installation/claude-desktop.md)参照）
- Dockerがインストール済み（[Docker セットアップガイド](../../../getting-started/installation/docker.md)参照）
- 基本的なターミナル操作の知識

## PubMed MCPサーバーのセットアップ

### 1. リポジトリのクローン

まず、このチュートリアルのリポジトリをクローンします：

```bash
git clone https://github.com/fuku-inc/life-science-agent-tutorial.git
cd life-science-agent-tutorial/tutorials/02-mcp-server/claude-desktop/pubmed-search
```

### 2. Dockerイメージのビルド

PubMed MCPサーバーのDockerイメージをビルドします：

```bash
docker build -t pubmed-mcp-server .
```

!!! info "初回ビルド時の注意"
    初回ビルド時は依存パッケージのダウンロードが行われるため、数分かかる場合があります。

### 3. Claude Desktopの設定

Claude Desktopの設定ファイルを開きます：

=== "macOS"
    ```bash
    open ~/Library/Application\ Support/Claude/claude_desktop_config.json
    ```

=== "Windows"
    ```
    %APPDATA%\Claude\claude_desktop_config.json
    ```

設定ファイルの `mcpServers` セクションに以下の設定を追加します：

!!! warning "既存の設定を保持する"
    すでに他のMCPサーバーの設定がある場合は、既存の設定を削除せずに、`pubmed` の設定を追加してください。

```json
{
  "mcpServers": {
    // 既存の設定があればそのまま残す
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


### 4. Claude Desktopの再起動

設定を反映させるため、Claude Desktopを再起動します。

## 基本的な検索操作

### キーワード検索

Claude Desktopで以下のように入力してみましょう：

```
COVID-19のmRNAワクチンに関する2023年以降の論文を5件検索してください
```

MCPサーバーが自動的にPubMedにアクセスし、検索結果を返します。

### 検索結果の確認

検索結果には以下の情報が含まれます：

- 論文タイトル
- 著者リスト
- 掲載誌名
- 出版年
- PMID（PubMed ID）
- アブストラクト（要約）

## 高度な検索テクニック

### 著者名検索

特定の著者の論文を検索：

```
山中伸弥の最新の論文を10件検索してください
```

### 期間指定検索

特定期間の論文を検索：

```
2022年から2024年の間に発表されたCRISPR技術に関する論文を検索してください
```

### MeSHタームの活用

MeSH（Medical Subject Headings）を使った精密検索：

```
MeSHターム "Diabetes Mellitus, Type 2" を使って糖尿病の最新治療法に関する論文を検索してください
```

## 検索結果の整理と活用

### 要約の作成

```
検索した論文の主要な発見を箇条書きでまとめてください
```

### 研究トレンドの分析

```
検索結果から、この分野の研究トレンドを分析してください
```

### 引用情報の整理

```
検索した論文の引用情報をAPA形式でリストアップしてください
```

## 実践演習

### 演習1: COVID-19関連論文の検索

以下の課題に取り組んでみましょう：

1. COVID-19の長期後遺症（Long COVID）に関する最新の総説論文を5件検索
2. 検索結果から主要な症状と治療法をまとめる
3. 今後の研究課題を3つ挙げる

### 演習2: 特定著者の研究追跡

1. あなたの研究分野の著名な研究者を1人選ぶ
2. その研究者の過去3年間の論文を検索
3. 研究の変遷や新しい方向性を分析

## トラブルシューティング

#### 設定が反映されない

1. Claude Desktopを完全に終了（メニューから「Quit」を選択）
2. 設定ファイルのJSON構文を確認
3. Claude Desktopを再起動

### ログの確認

問題が解決しない場合は、Claude Desktopのログを確認してください。MCPサーバーのエラーメッセージがそこに表示されます。

## まとめ

このチュートリアルでは、以下のことを学びました：

- ✅ PubMed MCPサーバーのDocker環境での構築
- ✅ Claude Desktopとの連携設定
- ✅ 効率的な文献検索の実践
- ✅ 検索結果の整理と活用方法

これらのスキルを活用することで、研究に必要な文献調査の時間を大幅に短縮できます。

## 次のステップ

- 他のデータベース（UniProt、ChEMBL）のMCPサーバーも試してみる
- 複数のMCPサーバーを組み合わせて使用する
- 独自のMCPサーバーを開発する（[レベル3](../../../03-build-agents/index.md)へ）

---

### **関連リンク**:

- [Claude Desktopの基本に戻る](index.md)
- [他のMCPサーバーチュートリアルを見る](../index.md#学習内容)