# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 05:09:35 2019

@author: student
"""

import pandas

url = 'https://www.nikkei.com/nkd/company/history/dprice/?scode=7203&ba=1'

frame = pandas.read_html(url)[0]
csv = frame.to_csv()

with open('toyota_stock.csv', 'w') as f:
    print(csv, file=f)
