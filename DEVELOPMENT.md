# 開発者向けドキュメント

## ドキュメントの編集・確認

### ローカルでのドキュメント確認（Docker使用）

#### 1. 基本的な確認
```bash
# Docker イメージをビルド（ネットワーク問題がある場合はlegacy builderを使用）
DOCKER_BUILDKIT=0 docker build -t docs-server .

# サーバーを起動
docker run -p 8000:8000 docs-server
```

- ブラウザで `http://localhost:8000` にアクセス
- 静的なドキュメントが確認できる

#### 2. リアルタイム編集対応
```bash
# リアルタイム編集対応でサーバーを起動
docker run -p 8000:8000 \
  -v $(pwd)/docs:/docs/docs \
  -v $(pwd)/mkdocs.yml:/docs/mkdocs.yml \
  docs-server
```

- ファイルを編集すると自動的にブラウザがリロードされる
- 開発時はこちらを使用

#### 3. 開発時の便利なコマンド
```bash
# バックグラウンドで起動
docker run -d -p 8000:8000 \
  -v $(pwd)/docs:/docs/docs \
  -v $(pwd)/mkdocs.yml:/docs/mkdocs.yml \
  --name docs-server \
  docs-server

# ログを確認
docker logs docs-server

# 停止
docker stop docs-server
docker rm docs-server
```

### MkDocsの基本的な使い方

#### ファイル構造
```
docs/
├── index.md                 # トップページ
├── getting-started/
│   ├── index.md
│   ├── prerequisites.md
│   └── installation.md
├── tutorials/
│   ├── index.md
│   ├── 01-try-agents/
│   ├── 02-mcp-server/
│   ├── 03-build-agents/
│   └── 04-multi-agents/
└── resources/
    └── index.md
```

#### MkDocsの記法
- **Markdown**: 基本的なMarkdown記法を使用
- **Admonitions**: `!!! info`, `!!! warning`, `!!! tip` 等
- **タブ**: `=== "タブ名"` でタブ形式の表示
- **コードブロック**: バッククォート3つで囲む
- **リンク**: `[テキスト](リンク先)` 形式

#### 設定ファイル
- `mkdocs.yml`: サイト全体の設定
- `requirements.txt`: 依存関係の管理

### トラブルシューティング

#### よくある問題
1. **ポート競合**: 8000番ポートが使用中の場合
   ```bash
   # 別のポートを使用
   docker run -p 8001:8000 ...
   ```

2. **ファイルが反映されない**: ボリュームマウントの問題
   ```bash
   # 絶対パスで指定
   docker run -v /absolute/path/to/docs:/docs/docs ...
   ```

3. **イメージの更新が反映されない**: 
   ```bash
   # イメージを再ビルド
   docker build --no-cache -t docs-server .
   ```

#### ログの確認
```bash
# コンテナ内のログを確認
docker logs docs-server

# リアルタイムでログを確認
docker logs -f docs-server
```

### デプロイメント

#### GitHub Pages
- `main` ブランチにプッシュすると自動デプロイ
- GitHub Actions で `mkdocs gh-deploy` を実行

#### 手動デプロイ
```bash
# 静的ファイルをビルド
mkdocs build

# 生成されたファイルを確認
ls site/
```

### 開発の流れ

1. **ブランチ作成**: `git checkout -b feature/new-docs`
2. **Dockerサーバー起動**: リアルタイム編集モードで起動
3. **ドキュメント編集**: マークダウンファイルを編集
4. **動作確認**: ブラウザで確認
5. **コミット・プッシュ**: 変更をプッシュ
6. **プルリクエスト**: main ブランチへのマージ