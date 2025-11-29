## note Bot 概要

note Botとは、CLIからLINEにメッセージを送信できるLINE Botである。  
Pythonの実行環境があれば、本リポジトリのnotebot.pyに必要な値を設定することで使用することができる。  
noteBotは、Pythonファイルの実行によって起動することができる。  

別途LINE Developerに登録して、LINE Messaging API用の公式アカウント（noteBot用アカウント）を作成する必要がある。

### 使用技術

- Python
- LINE Messaging API

## 使用方法

note Bot の使用方法についてまとめる。

### 前提条件

- Python実行環境
- LINE Developerへの登録/ログイン
- LINE 公式アカウント（Bot用アカウント）の作成

### ①ファイルダウンロード

本リポジトリに含まれるnoteBot.pyをローカルにダウンロードしてください。

### ②LINE Messaging API の設定

```Python
CHANNEL_ACCESS_TOKEN = ""
USER_ID = ""
```

上記コードについて、トークンとIDをダブルクォート内に記述してください。  
設定完了後は保存して任意のディレクトリに配置してください。

### ③CLI起動

CLIならどれでも大丈夫です。  

### ④ファイルの実行（noteBot起動）

notebot.pyが置かれた任意のディレクトリに移動し、下記のコマンドを実行することで起動します。

```
python notebot.py
```

## 便利な利用方法

CLI起動時に毎回コマンドを打つのは大変ですが、アイコンのクリックによって簡単に起動することもできます。
