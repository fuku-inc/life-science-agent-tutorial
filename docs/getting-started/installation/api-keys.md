# API Key 設定ガイド

AIエージェントを利用するには、各サービスのAPI Keyが必要です。このガイドでは、主要なAIサービスのAPI Key取得と設定方法を説明します。

## OpenAI API Key

### 取得方法

1. [OpenAI Platform](https://platform.openai.com/)にアクセス
2. アカウントを作成またはログイン
3. 左側メニューの「API keys」をクリック
4. 「Create new secret key」ボタンをクリック
5. キーの名前を入力（例：「Agent Tutorial」）
6. 生成されたキーをコピー（一度しか表示されません）

### 料金体系

- 従量課金制（使用したトークン数に応じて課金）
- 無料クレジット：新規アカウントには$5程度の無料クレジット
- 料金詳細：[OpenAI Pricing](https://openai.com/pricing)

## Anthropic API Key

### 取得方法

1. [Anthropic Console](https://console.anthropic.com/)にアクセス
2. アカウントを作成またはログイン
3. 左側メニューの「API Keys」をクリック
4. 「Create Key」ボタンをクリック
5. キーの名前を入力（例：「Research Agent」）
6. 生成されたキーをコピー（一度しか表示されません）

### 料金体系

- 従量課金制（使用したトークン数に応じて課金）
- 無料プラン：月間の利用制限あり
- 料金詳細：[Anthropic Pricing](https://www.anthropic.com/pricing)

## API Keyの設定方法

### 環境変数での設定（推奨）

#### Windows (PowerShell)

```powershell
# ユーザー環境変数として設定
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-openai-key-here", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your-anthropic-key-here", "User")

# 確認
echo $env:OPENAI_API_KEY
echo $env:ANTHROPIC_API_KEY
```

#### macOS/Linux

```bash
# ~/.bashrcまたは~/.zshrcに追加
echo 'export OPENAI_API_KEY="your-openai-key-here"' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY="your-anthropic-key-here"' >> ~/.bashrc

# 設定を反映
source ~/.bashrc

# 確認
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY
```

### .envファイルでの設定（プロジェクト単位）

プロジェクトのルートディレクトリに`.env`ファイルを作成：

```env
# API Keys
OPENAI_API_KEY=your-openai-key-here
ANTHROPIC_API_KEY=your-anthropic-key-here

# その他の設定
MODEL_NAME=gpt-4
MAX_TOKENS=2000
TEMPERATURE=0.7
```

**重要**: `.env`ファイルは必ず`.gitignore`に追加してください：

```bash
echo ".env" >> .gitignore
```

## セキュリティのベストプラクティス

### 1. API Keyの保護

- **絶対にコードに直接記載しない**
- **GitHubなどの公開リポジトリにコミットしない**
- **他人と共有しない**

### 2. 利用制限の設定

#### OpenAI
1. [Usage limits](https://platform.openai.com/account/limits)で月間上限を設定
2. 異常な使用を検知するアラートを設定

#### Anthropic
1. Console内で利用上限を設定
2. 使用状況をモニタリング

### 3. キーのローテーション

- 定期的に新しいキーを生成（3ヶ月ごとを推奨）
- 不要になったキーは速やかに削除
- 漏洩の疑いがある場合は即座に無効化

## プログラムでの使用例

### Python

```python
import os
from openai import OpenAI
from anthropic import Anthropic

# 環境変数から取得
openai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

anthropic_client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)
```

### Node.js

```javascript
import OpenAI from 'openai';
import Anthropic from '@anthropic-ai/sdk';

// 環境変数から取得
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});

const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
});
```

## よくある質問

### API Keyが無効と表示される

1. キーが正しくコピーされているか確認（前後の空白に注意）
2. 環境変数が正しく設定されているか確認
3. 新しいターミナル/コマンドプロンプトで試す

### 利用制限に達した

1. 使用状況を各サービスのダッシュボードで確認
2. 必要に応じて有料プランにアップグレード
3. より効率的なプロンプトの使用を検討

### どのAPIを使うべきか

- **OpenAI (GPT-4)**: 汎用的なタスク、コード生成
- **Anthropic (Claude)**: 長文処理、研究論文の分析

## サポート情報

- **OpenAI Support**: [https://help.openai.com/](https://help.openai.com/)
- **Anthropic Support**: [https://support.anthropic.com/](https://support.anthropic.com/)

---

### **関連リンク**:

- [インストールガイドに戻る](index.md)
- [開発環境のセットアップ](dev-environment.md)
- [Claude Desktopのセットアップ](claude-desktop.md)