# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:29:16 2019

@author: student
"""

import pycurl
from io import BytesIO
from bs4 import BeautifulSoup

buffer = BytesIO()

#気象庁の積雪深データ
curl = pycurl.Curl()
curl.setopt(pycurl.URL, "http://www.data.jma.go.jp/obd/stats/data/mdrr/snc_rct/alltable/snc00.html")
curl.setopt(pycurl.WRITEFUNCTION, buffer.write)
curl.perform()

#BeautifulSoup4でスクレイピング
buffer_val = buffer.getvalue()
soup = BeautifulSoup(buffer_val, features="lxml")#html.parserでは失敗したのでlxmlで

def row_parser(row):
    tds = row.select("td")
    if(len(tds) > 10):#1行10セル以上ない行をはじく
       for td in tds:
           yield td.string

rows = (x for x in soup.select_one("table.data2_s").select("tr.mtx"))
cells = (list(row_parser(x)) for x in rows)
data = [r for r in cells if len(r) > 0]#空の行を弾く

#青森県の現在の積雪深のみ絞り込み、積雪深で降順ソート
aomori = [[r[0], r[1].replace("*", ""), str(r[2])] for r in data if r[0] == "青森県"]
for a in sorted(aomori, key=lambda x:x[2], reverse=True):
    print("{0}\t{1}\t{2}cm".format(*a))