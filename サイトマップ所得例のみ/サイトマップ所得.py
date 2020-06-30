# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:28:11 2020

@author: student
https://qiita.com/sawa---i/items/f1d8acb6ac026fedb3a9
"""

from bs4 import BeautifulSoup
import requests

urls = ''
path = './urls.txt'

# 対象サイトのサイトマップをGETする
r = requests.get("https://xxxxx..../sitemap")
c = r.content

# BeautifulSoupで対象ページのaタグを抜き出す
bs = BeautifulSoup(c, "html.parser")
a_list = bs.select("a")

# aタグをリンク部とテキスト部に分けていく
for a in a_list:
    name = a.get_text()
    link = a.get("href")
    urls += name + ':' + link
    urls += '\n'
    print(link, "\t", name)

# テキスト出力
with open(path, mode='w', encoding='UTF-8') as f:
    f.write(urls)
