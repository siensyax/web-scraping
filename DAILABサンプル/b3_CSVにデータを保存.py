# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:08:28 2019

@author: YAMADA HIDEYUKI
https://note.com/daikawai/n/nc73889d6d835
"""

'''
import pandas as pd
# pandasにはエクセルみたいに行列で構成するオブジェクトであるデータフレームという型がある


例そのまんま
# まずは列名を作成する

columns = ["Name", "Url"]  # 1行目に表示されるためのリストの宣言
df = pd.DataFrame(columns=columns) # 列名を指定する
# print(df)

# 今度は行を追加する
se = pd.Series(['LINEから送った画像を文字起こししてくれるアプリを作るときのメモ①', 'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns) # 行を作成
df = df.append(se, columns) # データフレームに行を追加
print(df)
'''
'''
TODO
1.以下の表のようになるように、データフレームを作成してください。
'''
# 普通にデータフレームを扱い方知らないからやり方わかるわけない
# 解答
import pandas as pd

columns = ["Name", "Url"]
df1 = pd.DataFrame(columns=columns) # 列名を指定する

# TODO1 以下の表のようになるように、データフレームを作成してください。
se = pd.Series(['データ解析の実務プロセス入門（あんちべ）』を読んで特に学びが多かったこと',
                'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'],
               columns) # 行を作成
df1 = df1.append(se, columns) # データフレームに行を追加
se = pd.Series(['sqlite3覚書 データベースに接続したり、中身のテーブル確認したり',
                'https://review-of-my-life.blogspot.com/2018/04/sqlite3.html'],
               columns) # 行を作成
df1 = df1.append(se, columns)
se = pd.Series(['LINEから送った画像を文字起こししてくれるアプリを作るときのメモ①',
                'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'],
               columns) # 行を作成
df1 = df1.append(se, columns)
# print(df1)

# 次に、作成したデータフレームをCSVに変換します。
# df.to_csv("ファイル名.csv")でcsvファイルを作成できます。

df1.to_csv("./例そのまんま.csv")
