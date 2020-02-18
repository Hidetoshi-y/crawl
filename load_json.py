from datetime import datetime
from datetime import timedelta
import pandas as pd
import csv 
import sys

def make_day_df(df, df_colum):#24回のループで1日分のDFを作る
    count = len(df['hourly']['data'])

    for i in range(count):
        df0 = df['hourly']['data'][i]#timeの取り出し
        df0['time'] = datetime.fromtimestamp(df0['time'])#UNIX時間→普通の時間
        #df0 = pd.DataFrame(df0.values(), index=df0.keys()).T
        df0 = pd.DataFrame(df0.values(), index=df0.keys()).T

        if i == 0:
            df_day = df0 #lsit→DataFrame 
        else:
            df_day = df_day.append(df0)
        
    return df_day

def daterange(_start, _end):
    for n in range((_end - _start).days):
        yield _start + timedelta(n)


if __name__ == "__main__":
    import json



start = datetime.strptime('2018-10-01', '%Y-%m-%d').date()
end   = datetime.strptime('2019-05-31', '%Y-%m-%d').date()

path = 'output/json/forecast-timemachine-2018-10-01.json'
with open(path) as f:#jsonを読み込む
    df = json.load(f)
df_colum = pd.DataFrame(index=df['hourly']['data'][0].keys()).T#全てのデータを入れるためのDFの作成

for times in daterange(start, end):#指定された日付から日付の回数繰り返す
    times = str(times)
    path = 'output/json/forecast-timemachine-'+times+'.json'
    with open(path) as f:#jsonを読み込む
        df = json.load(f)
    df_append = make_day_df(df, df_colum)#1日分の戻りDF

    #print(type(times))
    if times == str(start):#最初の一回だけはカラムが作られている空のDFにapeend
        df_data = df_colum.append(df_append)#カラムだけのDFに追加
    else:
        df_data = df_data.append(df_append)
print(df_data)


df_data.to_csv('output/to_csv_out.csv', encoding='utf-8')

    #df_append2 = df_append.append(df_append)
#print(df_append)
    #all_df.to_csv('output/to_csv_out.csv', encoding='utf-8')
#df_all = df_colum.append(df_data)





"""with open("output/darksky.csv", "w") as f: # 文字コードをShift_JISに指定
    writer = csv.writer(f, lineterminator="\n") # writerオブジェクトの作成 改行記号で行を区切る
    writer.writerows(all_df)"""
#print(type(all_df))

#all_df.to_csv('data/dst/to_csv_out.csv')




"""UNIX時間を西暦に直す処理
unix_time = df['hourly']['data'][0]['time']
normal_time = datetime.fromtimestamp(unix_time)

datetime.fromtimestamp(df['hourly']['data'][0]['time'])
print(normal_time)"""

