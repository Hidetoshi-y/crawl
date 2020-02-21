#!/bin/bash
# -*- coding: utf-8 -*-

def get_forecast_today(apikey, long, lati, uni):
    try:
        url = 'https://api.darksky.net/forecast/' + apikey + '/' + long + ',' + lati + '?' + 'units=' + uni + "&lang=ja"
        res = urllib.request.urlopen(url)
        # json_loads()でPythonオブジェクトに変換
        data = json.loads(res.read().decode('utf-8'))
        print(r'dataの取得を完了しました。')

    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    return data

def get_forecast_timemachine(apikey, long, lati, time, uni):
    try:
        url = 'https://api.darksky.net/forecast/' + apikey + '/' + long + ',' + lati +  ',' + time + '?' + 'units=' + uni + "&lang=ja"
        res = urllib.request.urlopen(url)
        # json_loads()でPythonオブジェクトに変換
        data = json.loads(res.read().decode('utf-8'))
        print(r'dataの取得を完了しました。')

    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    return data

if __name__ == "__main__":

    import argparse  
    import json
    import urllib.request
    from datetime import datetime
    from datetime import timedelta
    import time
    import configparser

    parser = argparse.ArgumentParser()

    #受け取る引数の追加
    parser.add_argument('--api', type=str, default='xxxxxxxx')
    parser.add_argument('--long', type=str, default='37.8267')
    parser.add_argument('--lati', type=str, default='-122.4233')
    parser.add_argument('--uni', type=str, default='si')
    parser.add_argument('--past', type=bool, default=None)
    parser.add_argument('--time', type=str, default='2019-11-15T00:00:00')
    args = parser.parse_args()
    
    APIKEY = args.api
    LONGITUDE = args.long
    LATITUDE = args.lati
    UNITS = args.uni
    NOW = args.past

    if NOW: 
            
        start = datetime.strptime('2018-10-01', '%Y-%m-%d').date()
        end   = datetime.strptime('2018-10-10', '%Y-%m-%d').date()

        def daterange(_start, _end):
            for n in range((_end - _start).days):
                yield _start + timedelta(n)

        #過去の一定期間を取り出す。
        for times in daterange(start, end):
            times = str(times)
            time = times+'T00:00:00'
            json_data = get_forecast_timemachine(apikey=args.api, long=args.long, lati=args.lati, uni=args.uni, time=time)
            with open('./output/test/forecast-timemachine-'+times+'.json', 'w') as fp:
                json.dump(json_data, fp, indent=4)
        print("過去の天気予報を獲得しました。")

    else:
        json_data = get_forecast_today(apikey=args.api, long=args.long, lati=args.lati, uni=args.uni)
    
        with open('./output/test/forecast.json', 'w') as fp:
            json.dump(json_data, fp, indent=4)
        print("今日の天気予報を獲得しました。")