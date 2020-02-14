#!/bin/bash
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    import argparse  
    import json
    import urllib.request
    import datetime
    import time
    import configparser

    parser = argparse.ArgumentParser()

    #受け取る引数の追加
    parser.add_argument('--api', type=str, default='aaxx')
    parser.add_argument('--long', type=str, default='37.8267')
    parser.add_argument('--lati', type=str, default='-122.4233')
    parser.add_argument('--uni', type=str, default='si')
    args = parser.parse_args()
    
    APIKEY = args.api
    LONGITUDE = args.long
    LATITUDE = args.lati
    UNITS = args.uni
    #EXCLUDE = currently,minutely,daily,alerts,flags
    

    def get_forecast():
        try:
            url = 'https://api.darksky.net/forecast/' + APIKEY + '/' + LONGITUDE + ',' + LATITUDE + '?' + 'units=' + UNITS + "&lang=ja"
            res = urllib.request.urlopen(url)
            # json_loads()でPythonオブジェクトに変換
            data = json.loads(res.read().decode('utf-8'))
            print(r'dataの取得を完了しました。')

        except urllib.error.HTTPError as e:
            print('HTTPError: ', e)

        except json.JSONDecodeError as e:
            print('JSONDecodeError: ', e)

        return data
    


    json_data = get_forecast()
    
    with open('./output/forecast-'+args.long+args.lati+'.json', 'w') as fp:
        json.dump(json_data, fp, indent=4)
    #change_data.to_csv("./output/"+args.long+args.lati+'.csv', encoding='utf-8')
    #print('Complete!')
