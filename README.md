# sumoto-garbage_separation.json

兵庫県洲本市のごみ・資源の分別データです。

data/sumoto-garbage-separation.jsonファイルにデータが入っています。

[ごみの出し方・分け方ガイドブック（保存版）](https://www.city.sumoto.lg.jp/uploaded/attachment/7092.PDF)から手作業で入力したデータです。

## 収載データ

- item(品目名)
- material(材質・用途など)
- kind(分別の種類)
- note(備考)

## 編集方法

Pythonを利用して簡易のチェックができます。

Pythonの環境構築後に`pip`にて必要なパッケージをインストールします。：

`$ pip install -r requirements.txt`

編集したらpytestを利用してデータを検証します。：

```
$ pytest test_json.py
================================================= test session starts =================================================
platform win32 -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: C:\projects\sumoto-garbage_separation
collected 3 items

test_json.py ...                                                                                                 [100%]

================================================== 3 passed in 0.02s ==================================================
```

データに問題がなければ緑の文字で`3 passed`と表示されます。

データに問題がなければ下記のコマンドでjsonデータの整形ができます。：

`$ python format.py`

## 間違いがあったら

jsonファイルは手作業で入力しています。そのため記載ミスがあるかもしれません。

間違いがあった場合はissueを作成するか、pull requestを送ってください。
