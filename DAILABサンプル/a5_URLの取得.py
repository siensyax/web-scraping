# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:08:34 2019

@author: YAMADA HIDEYUKI
https://note.com/daikawai/n/nc73889d6d835
"""

# Beautiful Soupのインポート
from bs4 import BeautifulSoup
# こちらで用意したHTML
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# BeautifulSoupの初期化
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化

# print(soup.a.get("href"))  # httpがあるhrefの部分だけを取り出す
'''
TODO
1. for文を利用して、aタグのURLをすべてprintしてください
'''
# まずはリスト形式でaタグを所得する
tags = soup.find_all("a")

# print(tags)

# 次に上で所得したリスト形式のtagsから取り出して表示する
# for tag in tags:
#     print(tag)

# 最後にtagsからhrefにあるhttpを取り出す
# aタグはsoupの時点ですでにfind_allで指定しているのでもう一回aメソッドをやるとNoneが返される
for tag in tags:
    print(tag.get("href"))
