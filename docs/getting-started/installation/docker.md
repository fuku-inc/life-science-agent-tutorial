# Docker セットアップガイド

Dockerは、レベル2以降で必要となるコンテナ実行環境です。MCPサーバーや開発環境を動かすために使用します。

## 必要なシステム要件

- **OS**: 
    - 本チュートリアルではmacOS、Linuxを推奨
    - Windowsの場合は一部機能に制限や予期しない動作が発生する可能性があります
- **メモリ**: 最低 4GB RAM

## ライセンスについて

**重要**: Docker Desktopの商用利用には以下の条件があります：

- **個人利用、教育、非商用オープンソース**: 無料
- **小規模企業** (従業員250名以下かつ年間売上$10M USD以下): 無料
- **大規模企業** (従業員250名超または年間売上$10M USD超): 有料サブスクリプションが必要

詳細は[Docker Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement/)を参照してください。

## インストール手順

お使いのOSに応じて、以下の公式インストールガイドを参照してください：

### macOS

Docker Desktop for Macの公式インストールガイド：

[https://docs.docker.com/desktop/setup/install/mac-install/](https://docs.docker.com/desktop/setup/install/mac-install/)

- Intel MacとApple Silicon (M1/M2) の両方に対応
- インストール後、メニューバーからDocker Desktopを起動

### Linux

Docker Desktop for Linuxの公式インストールガイド：

[https://docs.docker.com/desktop/setup/install/linux/](https://docs.docker.com/desktop/setup/install/linux/)

- Ubuntu、Debian、Fedora、Arch Linuxなど主要ディストリビューションに対応
- GUI環境がない場合は、Docker Engine単体のインストールも可能

### Windows

Docker Desktop for Windowsの公式インストールガイド：

[https://docs.docker.com/desktop/setup/install/windows-install/](https://docs.docker.com/desktop/setup/install/windows-install/)


## インストール後の確認

インストールが完了したら、以下のコマンドでDockerが正常に動作することを確認してください：

```bash
# Dockerのバージョン確認
docker --version

# 動作確認（Hello Worldコンテナの実行）
docker run hello-world
```

## サポート情報

問題が発生した場合は、以下の公式ドキュメントを参照してください：

- **Docker Desktop公式ヘルプ**: [https://docs.docker.com/desktop/troubleshoot/overview/](https://docs.docker.com/desktop/troubleshoot/overview/)
- **Docker Engine公式ドキュメント**: [https://docs.docker.com/engine/](https://docs.docker.com/engine/)
- **Dockerコミュニティフォーラム**: [https://forums.docker.com/](https://forums.docker.com/)

---

### **関連リンク**:

- [インストールガイドに戻る](index.md)