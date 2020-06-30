# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 04:30:37 2019

@author: student
https://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406
ver 2
所得した日経平均株価を前のやつと比較して違っていたらcsvを更新するようにする．
"""

import csv
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import request
import pandas as pd


# csvを追記モードで開きます
f = open('nikkei_heikin.csv', 'a')
writer = csv.writer(f, lineterminator='\n')
# csvに記述するレコードを作成します
csv_list = []
# 現在の時刻を年、月、日、と時、分、秒で取得します
date_ = datetime.now().strftime("%Y/%m/%d")
time_ = datetime.now().strftime("%H:%M:%S")
# CSVの1カラム目に日付を挿入します
csv_list.append(date_)
# CSVの2カラム目に時刻を挿入します
csv_list.append(time_)

url = "http://www.nikkei.com/markets/kabu/"  # アクセスするURL
# URLにアクセスする htmlが帰ってくる
# → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")  # htmlをBeautifulSoupで扱う
# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます
# →[<span class="m-wficon triDown"></span>, <span class="l-h...
span = soup.find_all("span")

# print時のエラーとならないように最初に宣言しておきます。
nikkei_heikin = ""
# for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
for tag in span:
    # spanタグの中でもclassの設定がされていない要素は、
    # tag.get("class").pop(0)を行うことのできずエラーとなるため、tryでエラーを回避する
    try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        if string_ in "mkc-stock_prices":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin = tag.string.replace(',', '')
            # 摘出が完了したのでfor分を抜けます
            break
    except:
        # パス→何も処理を行わない
        pass

# ひとつ前の日経平均株価をcsvから所得して，今サイトから入手した最新の株価が更新された場合のみ追記する
# csvファイルから最終行の株価を所得する
nikkei_heikin_pre = pd.read_csv('nikkei_heikin.csv')
nikkei_heikin_last = nikkei_heikin_pre.tail(1)['日経平均株価']
# 摘出した日経平均株価を更新があった場合のみ出力します。
'''
# そのための確認の残骸 一応きちんとデータは所得できている，結構平均株価はすぐに変化する
print(float(nikkei_heikin))
print(nikkei_heikin_last.values[0])  # pandasのSeriesはリスト型で値が返される
print(float(nikkei_heikin) == nikkei_heikin_last.values)
'''
if not float(nikkei_heikin) == nikkei_heikin_last.values:
    # 2カラム目に日経平均を記録します
    csv_list.append(nikkei_heikin)
    # csvに追記します
    writer.writerow(csv_list)

# ファイル破損防止のために閉じます
f.close()
