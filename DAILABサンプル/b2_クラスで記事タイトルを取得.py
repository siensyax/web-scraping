# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:28:53 2019

@author: YAMADA HIDEYUKI
https://note.com/daikawai/n/nc73889d6d835
"""

import requests
from bs4 import BeautifulSoup

# prettify()メソッドを使ってきれいにする
html_doc = requests.get("https://review-of-my-life.blogspot.com").text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化

# 今度はClassを指定して、記事のタイトルのみを取得してみます。
# find_allの引数に、辞書型でclassを指定することができます。
# print(soup.find_all("h3", {"class": "post-title"}))

'''
TODO
1. 記事名を取得してください。
2. 記事のURLを取得してください。
'''
titles = soup.find_all("h3", {"class": "post-title"})
for title in titles:  # リスト形式から取り出して表示させる
    # print(title)  # 元のｈｔｍｌすべてを表示
    # print(title.a)  # aタグのみを取りだして表示する
    # 1. 記事名を取得してください。
    print(title.a.string)  # aタグの中の文字だけを取り出して表示する

    # 2. 記事のURLを取得してください。
    # print(title.get("href"))  # 単にgetメソッド使ってもNoneが返ってくるだけ
    print(title.a.get("href"))  # aタグの中って指定してgetメソッドを使う