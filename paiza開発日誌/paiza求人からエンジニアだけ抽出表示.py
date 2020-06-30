# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:12:33 2019

@author: student
"""

import requests
import lxml.html

res = requests.get("https://paiza.jp/career/job_offers")
root = lxml.html.fromstring(res.text).getroottree()
print(root)
print(type(root))
print(root.xpath('//a[@class="titleLink"]'))

for i in root.xpath('//a[@class="titleLink"]'):
    # print(i)
    if "エンジニア" in i.text:
        print(i.text)
