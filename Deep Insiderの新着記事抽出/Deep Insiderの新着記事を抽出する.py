# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:15:15 2019

@author: student
"""

from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.atmarkit.co.jp/ait/subtop/di/'
response = request.urlopen(url)
soup = BeautifulSoup(response, features="lxml")
response.close()

# print(soup)
# print(soup.title)
# <title> Deep Insider - ＠IT</title>

# print(soup.head.title)
# <title> Deep Insider - ＠IT</title>
# print(soup.title.text)
# Deep Insider - ＠IT

topstories = soup.find('div', class_='colBoxTopstories')
# print(topstories)
colboxindexes = topstories.find_all('div', class_='colBoxIndex')
# print(colboxindexes[0])
'''
一回分
title = colboxindexes[0].select('div.colBoxTitle')[0].text
description = colboxindexes[0].select('div.colBoxDescription')[0].text
print(title, ':', description)
'''
'''
# 上の一回分を記事数だけ繰り返す，内法表記も使える
top_articles = []
for item in colboxindexes:
    title = item.select('div.colBoxTitle')[0].text
    description = item.select('div.colBoxDescription')[0].text
    top_articles.append(f'{title}: {description}')

for articles in top_articles:
    print(articles)
'''
# 別解，内法表記使ってる
titles = topstories.find_all('div', class_='colBoxTitle')
descriptions = topstories.find_all('div', class_='colBoxDescription')

title_and_descs = zip(titles, descriptions)
top_articles = [f'{item[0].text}: {item[1].text}' for item in title_and_descs]

for articles in top_articles:
    print(articles)
