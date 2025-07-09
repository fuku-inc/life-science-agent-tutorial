# インストールガイド

前提条件を確認したら、レベル別にソフトウェアをインストールしていきましょう。

## 📋 インストール手順の概要

各レベルに応じて必要なソフトウェアをインストールします：

- **レベル1**: Webブラウザのみ（既にインストール済み）
- **レベル2**: Docker + Git + テキストエディタ
- **レベル3**: 上記 + Python開発環境
- **レベル4**: 上記すべて + 追加ライブラリ

## 🌐 レベル1: Webブラウザ環境

### 必要なソフトウェア
レベル1では特別なインストール作業は必要ありません。

### 準備手順
1. **Webブラウザの更新**
   - Chrome: メニュー → ヘルプ → Google Chrome について
   - Firefox: メニュー → ヘルプ → Firefox について
   - Safari: Safari → Safari について
   - Edge: メニュー → ヘルプとフィードバック → Microsoft Edge について

2. **アカウント作成**
   - [OpenAI ChatGPT](https://chat.openai.com/)
   - [Anthropic Claude](https://claude.ai/)
   - [GitHub](https://github.com/)

✅ **完了確認**: 各サービスにログインできれば準備完了です！

## 🐳 レベル2: Docker環境の構築

### 1. Docker のインストール

#### Windows
1. [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)をダウンロード
2. インストーラーを実行
3. PCを再起動
4. Docker Desktopを起動
5. コマンドプロンプトで確認:
   ```bash
   docker --version
   ```

#### macOS
1. [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)をダウンロード
2. .dmgファイルを開いてアプリケーションフォルダにドラッグ
3. Docker Desktopを起動
4. ターミナルで確認:
   ```bash
   docker --version
   ```

#### Linux (Ubuntu)
```bash
# 必要なパッケージをインストール
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release

# Dockerの公式GPGキーを追加
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# リポジトリを設定
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Docker Engineをインストール
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

# バージョン確認
docker --version
```

### 2. Git のインストール

#### Windows
1. [Git for Windows](https://git-scm.com/download/win)をダウンロード
2. インストーラーを実行（デフォルト設定でOK）
3. Git Bashまたはコマンドプロンプトで確認:
   ```bash
   git --version
   ```

#### macOS
```bash
# Homebrewを使用（推奨）
brew install git

# または公式インストーラー
# https://git-scm.com/download/mac からダウンロード
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt install git

# CentOS/RHEL
sudo yum install git

# バージョン確認
git --version
```

### 3. テキストエディタのインストール

#### Visual Studio Code（推奨）
1. [VS Code](https://code.visualstudio.com/)をダウンロード
2. インストーラーを実行
3. 推奨拡張機能:
   - Python
   - Docker
   - GitHub Copilot（オプション）

#### 代替エディタ
- **Sublime Text**: [公式サイト](https://www.sublimetext.com/)
- **Atom**: [公式サイト](https://atom.io/)
- **メモ帳++**: [公式サイト](https://notepad-plus-plus.org/)

### 4. 動作確認

以下のコマンドを実行して、すべてのツールが正常にインストールされていることを確認:

```bash
# Docker
docker --version
docker run hello-world

# Git
git --version

# エディタ（VS Codeの場合）
code --version
```

## 🐍 レベル3: Python開発環境

### 1. Python のインストール

#### Windows
1. [Python公式サイト](https://www.python.org/downloads/)から最新版をダウンロード
2. インストーラーを実行
3. ⚠️ **重要**: "Add Python to PATH" をチェック
4. コマンドプロンプトで確認:
   ```bash
   python --version
   pip --version
   ```

#### macOS
```bash
# Homebrewを使用（推奨）
brew install python

# または公式インストーラー
# https://www.python.org/downloads/macos/
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip

# バージョン確認
python3 --version
pip3 --version
```

### 2. 仮想環境の設定

```bash
# 仮想環境の作成
python -m venv agent-tutorial-env

# 仮想環境の有効化
# Windows
agent-tutorial-env\Scripts\activate

# macOS/Linux
source agent-tutorial-env/bin/activate

# 確認
which python  # 仮想環境のPythonが表示されるはず
```

### 3. 基本パッケージのインストール

```bash
# 必要なパッケージをインストール
pip install --upgrade pip
pip install requests openai anthropic
pip install jupyter notebook
pip install pandas numpy matplotlib
```

### 4. API Key の設定

#### 環境変数の設定（推奨）

**Windows**:
```batch
setx OPENAI_API_KEY "your_openai_api_key_here"
setx ANTHROPIC_API_KEY "your_anthropic_api_key_here"
```

**macOS/Linux**:
```bash
# ~/.bashrc または ~/.zshrc に追加
export OPENAI_API_KEY="your_openai_api_key_here"
export ANTHROPIC_API_KEY="your_anthropic_api_key_here"

# 設定を反映
source ~/.bashrc  # または ~/.zshrc
```

#### .env ファイルの作成（代替手段）

```bash
# プロジェクトディレクトリに.envファイルを作成
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
echo "ANTHROPIC_API_KEY=your_anthropic_api_key_here" >> .env
```

⚠️ **重要**: .env ファイルは .gitignore に追加してください

## 🚀 レベル4: 高度な開発環境

### 1. 追加Pythonパッケージ

```bash
# 高度なライブラリをインストール
pip install fastapi uvicorn
pip install streamlit
pip install langchain
pip install autogen-agentchat
pip install crewai
```

### 2. 開発ツールの設定

#### デバッグ環境
```bash
# デバッグツール
pip install ipdb pytest
pip install black flake8  # コードフォーマッタ
```

#### IDE設定（VS Code）
1. **Python拡張機能**の詳細設定
2. **デバッガー**の設定
3. **Jupyter notebook**サポート

### 3. データベース環境（オプション）

#### SQLite（軽量）
```bash
pip install sqlite3
```

#### PostgreSQL（本格的）
```bash
# Docker でPostgreSQLを起動
docker run --name postgres-db -e POSTGRES_PASSWORD=mypassword -p 5432:5432 -d postgres
pip install psycopg2-binary
```

## ✅ インストール完了チェックリスト

### レベル1 チェック
- [ ] Webブラウザが最新版になっている
- [ ] OpenAI アカウントでログインできる
- [ ] Claude アカウントでログインできる
- [ ] GitHub アカウントでログインできる

### レベル2 チェック
- [ ] Docker が正常に動作する (`docker run hello-world`)
- [ ] Git が正常に動作する (`git --version`)
- [ ] テキストエディタが起動する

### レベル3 チェック
- [ ] Python が正常に動作する (`python --version`)
- [ ] pip が正常に動作する (`pip --version`)
- [ ] 仮想環境が作成・有効化できる
- [ ] 基本パッケージがインストールされている
- [ ] API Key が正しく設定されている

### レベル4 チェック
- [ ] 追加パッケージが正常にインストールされている
- [ ] 開発ツールが正常に動作する
- [ ] デバッグ環境が構築されている

## 🔧 トラブルシューティング

### よくある問題と解決方法

#### Docker関連
- **問題**: Docker が起動しない
- **解決**: 
  - Windows: Hyper-V が有効になっているか確認
  - macOS: システム設定で Docker へのアクセスを許可
  - Linux: Docker サービスが実行中か確認 (`sudo systemctl status docker`)

#### Python関連
- **問題**: Python が見つからない
- **解決**: 
  - PATH環境変数を確認
  - Python インストール時に "Add to PATH" をチェック
  - コマンドプロンプト/ターミナルを再起動

#### API Key関連
- **問題**: API Key が認識されない
- **解決**: 
  - 環境変数の設定を確認
  - ターミナルの再起動
  - .env ファイルの場所と内容を確認

### サポートリソース

- **GitHub Issues**: [プロジェクトリポジトリ](https://github.com/fuku-inc/life-science-agent-tutorial/issues)
- **公式ドキュメント**: 各ツールの公式ドキュメント
- **コミュニティ**: 研究者向けSlackやDiscord

## 🎯 次のステップ

インストールが完了したら、実際のチュートリアルを開始しましょう！

[▶️ チュートリアルを開始](../tutorials/){ .md-button .md-button--primary }

!!! success "インストール完了！"
    すべてのツールが正常にインストールされました。
    今度は実際にAIエージェントを使った研究を始めましょう！

!!! tip "学習のコツ"
    - 少しずつ進めて、一つずつ確実に理解していきましょう
    - 実際の研究データで練習すると効果的です
    - 困ったときは遠慮なく質問してください

!!! warning "セキュリティについて"
    - API Key は絶対に他人と共有しないでください
    - 研究データの取り扱いについては、各サービスの利用規約を必ず確認してください
    - 定期的にソフトウェアを最新版にアップデートしてください