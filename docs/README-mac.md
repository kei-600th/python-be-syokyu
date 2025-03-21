# 環境構築

※当テキストは Railway 問題文から参照するテキストをリポジトリ自体にも残しておくためのテキスト。

## 概要

Python Railway の問題を解くために必要な下記ツールのインストール方法と環境構築の手順を解説します。
- Python 3.12
- Docker
- Visual Studio Code
- Git

上記のうち、Visual Studio Code と Git についてのインストール方法は、
[Railway 準備編](https://www.notion.so/techbowl/Railway-ceba695d5014460e9733c2a46318cdec) をご確認いただき、挑戦の準備をしてください。

その他リポジトリの更新の仕方や、トラブルシューティングについても上記の Railway 準備編にございます。
何かあった際は、まずそちらを確認しましょう。

## 手順
1. Python のセットアップ
    - [こちら](./instructions/00_install_python/install_python_mac.md) を参照ください。
1. Docker のセットアップ
    - [こちら](./instructions/10_install_docker/install_docker_mac.md) を参照ください。
2. ローカルサーバが立ち上がっていることを確認
    - [http://localhost:18008/docs](http://localhost:18008/docs) にアクセスし、ローカルサーバが立ち上がっていることを確認します。
3. 環境構築完了後の確認
    - 環境構築が正常に終了したことを確認するために、Visual Studio Code でリポジトリを開いてから、ファイルの変更や追加ができるか確認してください。
    - また、TechTrain Railway の拡張機能が正しく機能しているかも確認してください。
---
以上で Python Backend Railway に取り組むための環境が整いました。
Visual Studio Code を使用してコードを編集し、「TechTrain Railway」という拡張機能から「できた!」と書かれた青いボタンをクリックすると判定が始まります。
