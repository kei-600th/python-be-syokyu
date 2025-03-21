# Python 環境セットアップ - macOS 編

この手順では macOS 環境下における `Python 3.12` のインストール手順を説明しています。
※他のバージョンでも動く可能性はありますが、動作を安定させるために上記のバージョンでインストールすることをおすすめいたします。

## 前提
- [Railway 準備編](https://techbowl.notion.site/Railway-ceba695d5014460e9733c2a46318cdec)にて必要なツールのインストールが完了していること。 ( ここでは homebrew がインストール済みであることを前提としています。 )

## Python のインストール
1. Mac ユーザーの場合、 Homebrew でインストールを行います。
    1. `brew install python@3.12`
2. インストール実行が正常に完了後、ターミナルで以下コマンドを実行し、バージョンが表示されていればインストールが行えています。
    1. `python3.12 -V`

## 仮想環境のセットアップ
ローカルにインストールした Python では、 Python 標準だけの機能だけでなく、
アプリケーション開発を効率的に行うため必要な Python 用パッケージをインストールして使用することが多くの場合必要となります。

( FastAPI や numpy 、pandas も Pythonパッケージの一つ )

Python 用パッケージのインストールには、
ここでは、[pip](https://packaging.python.org/ja/latest/key_projects/#pip) という Python パッケージ管理ツールを使用します。

Python パッケージ管理ツールには pip 以外にもさまざまなものがありますが、最も広く使われており、最近の Python には同梱されていることから、この Railway では pip を使用します。

1. ローカル Python 環境の仮想環境を作成し、VSCode で開いているプロジェクトに適用する。
    1. VSCode でコードを編集する際は、ローカル環境上となり、 VSCode の構文解析等を有効に働かせるためにローカル環境でも Python 環境を準備します。
    2. リポジトリを VSCode で開いた後、 VSCode 上でターミナルを開くとプロジェクト直下をカレントディレクトリとしてターミナルが開きます。
    3. その状態で以下コマンドを実行します。
        ```bash
        python3.12 -m venv .venv
        ```
        このコマンドを実行すると、プロジェクト直下に`.venv`ディレクトリが作成されます。
    4. VSCode にて「 Cmd + Shift + P 」で VSCode のコマンドパレットを開きます。コマンドパレットにて「`Python: インタープリターを選択`」を選択します。

        以下のように途中まで入力すると選択肢が絞られていって見つけやすくなると思います。
        ![](../../images/vscode_select_python_interpreter.png)
    5. 選択後、インタープリターの一覧が表示されますが、以下の`./.venv/bin/python`がパスとして表示されているものを選択してください。
        ![](../../images/vscode_python_interpreter_list.png)
    6. 上記で対応完了となります。現在どこの Python インタープリターが選択されているかは、VSCode で`.py`ファイルを開くと、VSCode のウィンドウ最下部に表示されます。
        ![](../../images/vscode_current_python_interpreter.png)
    7. また、`.venv`配下の Python インタープリターを選択していると、VSCode 上でターミナルを新規で開いた時に予めターミナル上でも venv の仮想環境が有効になった状態でターミナルが起動されます。
    ![](../../images/vscode_terminal_with_venv.png)
    →「(.venv)」という文言が表示されている。
2. 利用する Python パッケージを Python 仮想環境配下にインストールする。
    1. 上記の手順にて VSCode のターミナルで venv が有効になっている状態で立ち上がる旨を説明しました。
    2. venv が有効化されている状態のターミナルで以下を実行し、仮想環境下で必要な Python パッケージをインストールします。
        ```bash
        pip install -r ./infra/docker/app/requirements/dev.txt
        ```
        ※アップデートを促されることもありますが、こちらはアップデートしても問題ございません。
