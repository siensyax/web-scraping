# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:45:57 2019

@author: YAMADA HIDEYUKI
https://note.com/daikawai/n/nc73889d6d835
"""

URL = "https://review-of-my-life.blogspot.com/"

'''
# Requests: WebページのHTMLを取得しよう
import requests
response = requests.get(URL)
print(response.text)
# このようにrequestsのgetメソッドを使うと指定したURLの全htmlを所得できる
'''
import requests
from bs4 import BeautifulSoup

# prettify()メソッドを使ってきれいにする
html_doc = requests.get("https://review-of-my-life.blogspot.com").text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
# print(soup.prettify())

'''
TODO
1. このページのaタグをすべて抜き出してください。(HTMLの内容)
2. このページのaタグのテキストのみを抜き出してください
3. このページのaタグのURLのみを抜き出して下さい
'''

# まずはaタグを1個だけ取り出す
# print(soup.a)

# 次はaタグすべてをリスト形式で所得する
# print("1. このページのaタグをすべて抜き出してください。(HTMLの内容)")
# print(soup.find_all("a"))

# 次はテキストのみを取り出す
# print(soup.find_all("a").string)  # だとリスト形式だからエラーになる

tags = soup.find_all("a")  # リスト形式のやつを仮の変数tagsに入れておく
# リスト形式のtagsをforでtagの中に別々に入れる
# for tag in tags:
#     print(tag)
# リスト形式から取り出したstr型のtagをstringメソッドでテキストのみにして表示させる
# print("2. このページのaタグのテキストのみを抜き出してください")
# for tag in tags:
#     print(tag.string)

# 最後にaタグの中のURLだけを取り出す
# getメソッドを使う
# まずは一つだけ取り出してgetメソッドの確認
# print(soup.a.get("href"))
print("3. このページのaタグのURLのみを抜き出して下さい")
for tag in tags:
    print(tag.get("href"))
