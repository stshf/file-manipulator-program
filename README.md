# File Manipulator Program
これは、テキストファイルの内容を反転、コピー、複製、文字列置換などの操作を行うコマンドラインツールです。
このプロジェクトは、プログラミング学習サイト[Recursion](https://recursionist.io/)の課題として作成されました。

## 課題の出典

この課題は、Recursionの以下のレッスンから出題されています：
[https://recursionist.io/dashboard/course/21/lesson/1086](https://recursionist.io/dashboard/course/21/lesson/1086)
※有料プラン

## 機能

- ファイル内容の反転
- ファイル内容のコピー
- ファイル内容の指定回数の複製
- ファイル内の文字列置換

## 必要条件

- Python 3.6以上

## インストール方法

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/file-manipulator.git
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd file-manipulator-program
   ```

## 使用方法

基本的な使用構文は以下の通りです：

```
python file_manipulator.py <コマンド> <入力ファイル> <出力ファイル> [追加の引数]
```

### 利用可能なコマンド：

1. ファイル内容の反転：
   ```
   python file_manipulator.py reverse input.txt output.txt
   ```

2. ファイル内容のコピー：
   ```
   python file_manipulator.py copy input.txt output.txt
   ```

3. ファイル内容の複製：
   ```
   python file_manipulator.py duplicate-contents input.txt output.txt <複製回数>
   ```

4. ファイル内の文字列置換：
   ```
   python file_manipulator.py replace-string input.txt output.txt <対象文字列> <新しい文字列>
   ```

## 使用例

1. ファイル内容を反転する：
   ```
   python file_manipulator.py reverse 例.txt 反転例.txt
   ```

2. ファイルをコピーする：
   ```
   python file_manipulator.py copy 原本.txt コピー.txt
   ```

3. ファイル内容を3回複製する：
   ```
   python file_manipulator.py duplicate-contents 入力.txt 3倍.txt 3
   ```

4. ファイル内の全ての「こんにちは」を「やあ」に置換する：
   ```
   python file_manipulator.py replace-string 挨拶.txt 新挨拶.txt こんにちは やあ
   ```

## エラー処理

このツールには、ファイル操作に関する基本的なエラー処理が含まれています。ファイルの読み書き中にエラーが発生した場合、適切なエラーメッセージが表示されます。

## ライセンス

このプロジェクトはRecursionの課題として作成されました。コードの使用や配布に関しては、Recursionの利用規約に従ってください。個人的な学習目的以外での使用は、事前にRecursionの許可を得る必要がある場合があります。

## 謝辞

このプロジェクトは、[Recursion](https://recursionist.io/)のカリキュラムの一部として作成されました。プログラミング学習の機会を提供してくださったRecursionに感謝いたします。
