# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:42:09 2019

@author: YAMADA HIDEYUKI
"""

import requests
from bs4 import BeautifulSoup

# htmlそのままを入手して表示させる、コードを改行なしでそのまま続けて表示
response = requests.get("https://review-of-my-life.blogspot.com/")
# print (response.text)

# HTMLを階層構造が分かるように少し整形して表示させる
html_doc = requests.get("https://review-of-my-life.blogspot.com").text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
# print(soup.prettify())  # インデントを整えてくれるコマンド

'''
# TODO1 このページのaタグをすべて抜き出してください。(HTMLの内容)
real_page_tags = soup.find_all("a")  # aタグが含まれた部分すべてをリスト形式で表示する
for tag in real_page_tags:
    print(tag)
'''

'''
# TODO2 このページのaタグをすべて抜き出してください。(HTMLの内容)
real_page_tags = soup.find_all("a")
for tag in real_page_tags:  # 上で作ったリストのタグで囲われたテキスト部分だけを表示する
    print(tag.string)
'''


# TODO3 このページのaタグをすべて抜き出してください。(HTMLの内容)
real_page_tags = soup.find_all("a")
for tag in real_page_tags:
    print(tag.get("href"))  # 上で作ったリストの中でハイパーリンクだけを取りだす
