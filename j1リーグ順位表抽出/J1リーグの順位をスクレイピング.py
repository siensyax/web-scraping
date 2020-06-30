# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:48:21 2019

@author: student
"""

from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.jleague.jp/standings/j1/'
response = request.urlopen(url)
soup = BeautifulSoup(response, features="html.parser")
response.close()

# print(response)
# print(soup)

header = soup.find('tr')
# print(header)

table = soup.find_all('tr')
# print(table[1])

# ほとんど問題ないが、チーム名がリンクになっていることから1つのtdタグにチーム名が2回登場している
# そのため、単純にtext属性でチーム名を得ようとすると、うまくいかない。そのため、ちょっと対処が必要になる。
# この後は先ほども言ったように、trタグを検索して、見出し行とチームごとの情報を含んだリストを得たら、
# 今度はその各行に対して、tdタグを検索して上に示した情報を抽出していくだけだ。
# 実際の部分
table = soup.find_all('tr')

standing = []
for row in table:
    tmp = []
    for item in row.find_all('td'):
        if item.a:
            tmp.append(item.text[0:len(item.text) // 2])
        else:
            tmp.append(item.text)
    del tmp[0]
    del tmp[-1]
    standing.append(tmp)

for item in standing:
    print(item)
