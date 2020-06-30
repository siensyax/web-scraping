# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:04:23 2019

@author: YAMADA HIDEYUKI
"""

# 1 requestsで、指定されたURLのHTMLを取得してください。
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://review-of-my-life.blogspot.com"
response = requests.get(url).text
# print(response)
# 1 requestsでrequestsで取得したHTMLをBeautifulSoupで呼び出してください。
soup = BeautifulSoup(response, 'html.parser') # BeautifulSoupの初期化
# print(soup.prettify())
# 1. 記事タイトルのh3とクラス名で指定して複数取得し、tagsに格納してください
tags = soup.find_all("h3", {"class": "post-title"})
# print(tags)
'''
TODO
・データフレームで列を作成
・for文でtagsを回す
　・tagから、記事名を取得
　・tagから、記事URLを取得
　・pandasのSeriesに記事名と記事URLを代入
　・データフレームに追加
・最後にCSVにして出力
'''
# ・データフレームで列を作成
columns = ["Name", "Url"]
# print(columns)
df = pd.DataFrame(columns=columns) # 列名を指定する
# print(df)

# ・for文でtagsを回す
for tag in tags:  # リスト形式から取り出して表示させる
    # ・tagから、記事名を取得
    titles = tag.a.string  # aタグの中の文字だけを取り出して表示する
    # ・tagから、記事URLを取得
    URLs = tag.a.get("href")  # aタグの中って指定してgetメソッドを使う
    # pandasのSeriesに記事名と記事URLを代入
    se = pd.Series([titles, URLs],columns)
    # データフレームに追加
    df = df.append(se, columns)

print(df)
print(type(df))

df.to_csv("./result..csv", encoding = 'utf-8-sig')
# encodingっを指定しないと文字化けしまくる
