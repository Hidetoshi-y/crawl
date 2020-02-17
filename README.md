# crawl

# 参考にしたサイト
(pythonでDarkSkyを利用)[https://qiita.com/snuow/items/29310b6d6229ce09caed]
https://qiita.com/masuraoProg/items/41d57671bc1ba89489bb
https://darksky.net/dev/docs
https://darksky.net/dev/account
https://knowledge.moshimore.jp/entry/dark_sky_api

# How to Use
通常の1日分取得
`python crawl_wather.py --api [APIキー] --long [緯度] --lati [経度] --uni [摂氏とか華氏]`

過去の1日分取得
`python crawl_wather.py -- api [APIキー] --long [緯度] --lati [経度] --time [過去の時間] --uni [摂氏とか華氏]`
過去の時間は 2019-11-11T00:00:00と指定する。　時間は意味なさそう。

# 項目
hourly以下に1日分（24個）のデータが入っている。
apparentTemperatureに一時間毎の温度予報が入っている。