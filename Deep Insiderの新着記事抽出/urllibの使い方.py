# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:27:12 2019

@author: student
"""

import urllib
url = "https://www.google.co.jp/"
html = urllib.request.urlopen(url=url).read().decode("shift-jis")
print(html)
