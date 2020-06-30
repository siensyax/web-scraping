#  -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:42:58 2019

@author: student
結局元のコードの時とは読売新聞側の構造が変わってうまくできんくなり
何とかできるようにしたかったがページ構造の中から最新ニュースっぽいところは見つけれたが
それをhmtlのヘッダを抜いて表示させるやり方が分からなかった
"""

from urllib import request
from bs4 import BeautifulSoup


def scraping():
    # url
    url = "http://www.yomiuri.co.jp/"

    # get html
    html = request.urlopen(url)

    # set BueatifulSoup
    soup = BeautifulSoup(html, features="html.parser")

    # get headlines
    # print(soup)

    mainNewsIndex = soup.find_all("h3", attrs={"class", "c-list-title c-list-title--small"})
    print(mainNewsIndex)
    print(type(mainNewsIndex))
    # <>に挟まれた部分を消去できればうまく成形できる
    # 本当はmainNewsIndexの中の<a>と</a>で区切られた部分を抽出でもいいがやり方わからん

    # headlines = mainNewsIndex.find_all("a")
    # print(headlines)
    # print headlines
    # for headline in headlines:
        # print(headline.contents[0], headline.span.string)



if __name__ == "__main__":
    scraping()
