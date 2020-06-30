# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:27:06 2020

@author: student
"""

import pandas as pd


csv_name = 'nikkei_heikin.csv'

nikkei_heikin_list = pd.read_csv(csv_name)


# 欠損データの割合を可視化関数
def kesson_table(df):
    null_val = df.isnull().sum()
    percent = 100 * df.isnull().sum()/len(df)
    kesson_table = pd.concat([null_val, percent], axis=1)
    kesson_table_ren_columns = kesson_table.rename(
    columns = {0 : '欠損数', 1 : '%'})
    return kesson_table_ren_columns


# print(nikkei_heikin_list.shape)  #読み込んだcsvのデータ数を可視化
# print(kesson_table(nikkei_heikin_list))  # データの欠損率を可視化
# 最終行を所得
# print(nikkei_heikin_list.tail(1))  # できた

# 最終行の株価の値のみを抽出して変数に代入
nikkei_heikin_last = nikkei_heikin_list.tail(1)['日経平均株価']
