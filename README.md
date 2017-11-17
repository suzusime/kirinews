# kirinews
きりたんにニュースを読み上げてもらう簡易スクリプト

## 概要
NHKニュースのRSSを取得し、その内容を東北きりたん（他VOICEROID）に読み上げてもらいます。

また、標準出力にはMarkdownでその内容を表示します。

## 要求
- `$ tk 文字列` で文字列をVOICEROIDに読み上げてもらえるような環境があること。
  - [VOICEROID+EXをコマンドラインからしゃべらせる](https://hgotoh.jp/wiki/doku.php/documents/voiceroid/voiceroid-002) の `echoseika.exe` を `tk.exe` とでもしてパスを通しておくのが手軽です。又はコードの`tk`の部分を書き換えて`echoseika`にしてもかまいません。
  
  - `■` でウエイトがかかることを想定して作っています。そのあたりは適宜コードを調整してください。
- python 3.6

## 使い方
```bash
$ python kirinews.py
```

## ライセンス
The MIT License
