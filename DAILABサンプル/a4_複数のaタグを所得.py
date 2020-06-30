# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:53:23 2019

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

'''
TODO
1. for文を利用して、取得したaタグのHTMLを含む部分をprintしてください。
2. for文を利用して、取得したaタグのHTMLを含まない部分だけprintしてください。
'''

# print(soup.a)  # aタグ全体から最初の一つだけを見つけてくる
# print(soup.find("a"))  # aタグ全体から最初の一つだけを見つけてくる

# 3つあるaタグをすべて所得するにはfind_allメソッドを利用する
# print(soup.find_all("a"))  # find_allメソッドはすべて所得してリスト形式で返す

# リスト形式の中からすべての要素を一つずつ抜き出す
# つまりリスト形式ではなく3つのstr形式で取り出す
# そのためにはforを使ってやる

a_tags = soup.findAll("a")
for a_tag in a_tags:
    print(a_tag)
    print(a_tag.string)
# こうやってやってやるとちゃんと[]で囲われたリスト形式でなくなる

'''
# 解答
tags = soup.find_all("a")
# for文を利用して、取得したaタグのHTMLを含む部分をprintしてください。
print("1. ")
for tag in tags:
   print (tag)
# for文を利用して、取得したaタグのHTMLを含む部分をprintしてください。
print("2. ")
for tag in tags:
   print (tag.string)
'''
