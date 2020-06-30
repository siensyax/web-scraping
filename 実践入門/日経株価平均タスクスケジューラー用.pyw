# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 04:30:37 2019

@author: student
https://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406
"""

import csv
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import request

# csvを追記モードで開きます
f = open('nikkei_heikin.csv', 'a')
writer = csv.writer(f, lineterminator='\n')
# csvに記述するレコードを作成します
csv_list = []
# 現在の時刻を年、月、日、時、分、秒で取得します
time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
# CSVの1カラム目に時間を挿入します
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

# 摘出した日経平均株価を出力します。
# 2カラム目に日経平均を記録します
csv_list.append(nikkei_heikin)
# csvに追記します
writer.writerow(csv_list)
# ファイル破損防止のために閉じます
f.close()
