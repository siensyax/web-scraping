# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:23:41 2019

@author: student
"""

import requests, lxml.html, io
from PIL import Image

res = requests.get("http://paiza.hatenablog.com")
root = lxml.html.fromstring(res.text).getroottree()

# 画像の場所を取得
print(root.xpath('//img')[0].attrib['src'])

# 画像を取得
res = requests.get(root.xpath('//img')[0].attrib['src'])

# 1画素のRGBを取得
image = Image.open(io.BytesIO(res.content))
print(image.getpixel((0, 0)))
image.show
