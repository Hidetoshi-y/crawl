# crawl

# 参考にしたサイト
(pythonでDarkSkyを利用)[https://qiita.com/snuow/items/29310b6d6229ce09caed]
https://qiita.com/masuraoProg/items/41d57671bc1ba89489bb
https://darksky.net/dev/docs
https://darksky.net/dev/account
(項目名)[https://knowledge.moshimore.jp/entry/dark_sky_api]

日付のforループ
https://qiita.com/chatrate/items/21b5c83ecf9197e64299
https://qiita.com/calderarie/items/0ef921b476911a55148d

(UNIX時間を日時datetimeに変換)[https://note.nkmk.me/python-unix-time-datetime/]

(辞書型をDFに変換)[https://qiita.com/ShoheiKojima/items/30ee0925472b7b3e5d5c]

(CSVの保存)[]


# How to Use
通常の1日分取得
`python crawl_wather.py --api [APIキー] --long [緯度] --lati [経度] --uni [摂氏とか華氏]`

過去の1日分取得
`python crawl_wather.py -- api [APIキー] --long [緯度] --lati [経度] --time [過去の時間] --uni [摂氏とか華氏]`
過去の時間は 2019-11-11T00:00:00と指定する。　時間は意味なさそう。

JsonデータをCSVにする。
`python load_json.py`

# 項目
hourly以下に1日分（24個）のデータが入っている。 0:00~23:00
apparentTemperatureに一時間毎の温度予報が入っている。

# 履歴
1.DarkSkyからクローリングを行なって2018-10-01 ~ 2019-5-30 までの天気予報のjsonファイルを獲得

jon>hourly>data
dataの下にkey と　Valueがある。

 Key  value
|time|時刻|

2.時刻はUNIX時間→普通の日付時間に変更

3.keyをカラム　Valueを値として辞書型をDF にする。

4.DFに辞書型を追加

5.24時間分の天気予報をDFにする関数を定義
5-1. 時刻はUNIX時間→普通の日付時間に変更

6.指定期間分のループで巨大なDFを作成

7.CSVを保存する.

