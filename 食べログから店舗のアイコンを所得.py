# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:49:06 2019

@author: YAMADA HIDEYUKI
"""

from bs4 import BeautifulSoup
from urllib import request

url = 'https://tabelog.com/hokkaido/A0110/A011003/1044881/'

response = request.urlopen(url)
soup = BeautifulSoup(response, features="html.parser")
response.close()

# print(soup)


id_con = soup.find('div', id='container')

# print(container.text)


# jpy = soup.select_one("jpy").string
# renewal = logo.select_one("renewal")
# print(renewal)  # これではうまく指定できなかった
# ほしいものがタグの中にのものだからうまくできんかも
# 業態変更 rst-status-badge-large rst-st-change-business

# 見つかりません
logo = id_con.find("span", class_="rst-status-badge-large rst-st-closed")
print(logo)

# print(logo.a.get("rst-st-closed"))
# aメソッドで指定してさらにgetメソッドを使ってみたが駄目だわ
# logoが欲しい部分はspanの中のclassにあるからうまくいかん
# spanやclassを指定できるメソッドはなかった
print(logo.a.get("href"))
# if not logo == None:
#     print("閉店")

'''
# 業態変更
logo = id_con.find("span", class_="rst-status-badge-large rst-st-change-business")
if not logo == None:
    print("業態変更")

# 業態変更
logo = id_con.find("span", class_="rst-status-badge-large rst-st-change-business")
if not logo == None:
    print("業態変更")

# 業態変更
logo = id_con.find("span", class_="rst-status-badge-large rst-st-change-business")
if not logo == None:
    print("業態変更")

# 業態変更
logo = id_con.find("span", class_="rst-status-badge-large rst-st-change-business")
if not logo == None:
    print("業態変更")

# 業態変更
logo = id_con.find("span", class_="rst-status-badge-large rst-st-change-business")
if not logo == None:
    print("業態変更")

# 業態変更
logo = id_con.find("span", class_="rst-status-badge-large rst-st-change-business")
if not logo == None:
    print("業態変更")

# 業態変更
logo = id_con.find("span", class_="rst-status-badge-large rst-st-change-business")
if not logo == None:
    print("業態変更")
'''
