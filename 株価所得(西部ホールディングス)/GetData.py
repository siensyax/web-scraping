# coding: utf-8
from urllib import request
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

#code = u"998407.o"
code = u"9024.T"
url = u"http://m.finance.yahoo.co.jp/stock/historicaldata?code=" +code
#url = u"http://stocks.finance.yahoo.co.jp/stocks/detail/?code=" + code
#url= u"http://stocks.finance.yahoo.co.jp/stock/historicaldata?code=9024.T&fy=2016&fm=9&fd=16&ty=2016&tm=8&td=16&cp=d"
html = request.urlopen(url)
soup = BeautifulSoup(html,features="lxml")
#print(soup)
# 株価を取得
# td class="stoksPrice"を検索

dateIndex = 0
elementIndex =0
elementNumber = 9
stockHistoryData = np.zeros([50,elementNumber])  #配列の宣言

"""
配列の説明
0:年
1:月
2:日
3:始値
4:高値
5:安値
6:終値
7:出来高
8:調整後終値
"""
for price in soup.find_all("table",class_="tableFin"):		#elementclint = 0

    for priceTable in price.find_all("td"):

			#日付をスライスで三つに分割する
            if elementIndex < 3:
                print(priceTable.string.split("/"))
                for i in priceTable.string.split("/"):
                    print(i)
                    stockHistoryData[dateIndex,elementIndex] = i
                    elementIndex +=1
            else:
                fixedElement = int(priceTable.string.replace(",",""))
                print(fixedElement) #ここは出力される。
                # elementclint +=1
                stockHistoryData[dateIndex,elementIndex] = fixedElement
                elementIndex +=1
#print(stockHistoryData[dateIndex,elementIndex]	)
            if elementIndex ==9:
                dateIndex +=1
                elementIndex = 0
                print(dateIndex)
#return stockHistoryData
#print(stockHistoryData)

###############################
#ATR の算出
###############################
#ATRのを入れる配列を作る
TR_list = np.zeros([19])
#20回繰り返し -> そうではなく、要素の数値だと思うが、結局は差分の検出だから19になる。

for i in range(19): #iは日付📅となる。0が最新となる。前日はインデックスを一つマイナスする。
	#ひとつずつ計算。絶対値。

	#1 Ａ＝当日高値－前日終値
    TR_A = abs(stockHistoryData[i,4] - stockHistoryData[i+1,8])
	#2 Ｂ＝前日終値－当日安値
    TR_B = abs(stockHistoryData[i+1,8] - stockHistoryData[i,5])
	#3 Ｃ＝当日高値－当日安値
    TR_C = abs(stockHistoryData[i,4] - stockHistoryData[i,5])

	#いずれか大きいものを判断し配列に格納。
    TR_list[i] = max(TR_A,TR_B,TR_C)

print(TR_list)
#SMA算出 当日のATR＝（前日のATR×19＋当日のTR×２）÷21 => 当日のATR＝（前日のATR×18＋当日のTR×2）÷20
#まずは、前日までのATR
Yesterday_ATR_list = np.zeros([18])
for i in range(1,19):
    Yesterday_ATR_list[i-1] = TR_list[i]
Yesterday_ATR = np.mean(Yesterday_ATR_list)
print(Yesterday_ATR_list)
print(Yesterday_ATR)
#
ATR = (Yesterday_ATR *18 + TR_list[0]*2 ) / 20

print(ATR)

###############################



"""
averageDates=5
getAverage = np.zeros(averageDates)

for i in range(0,averageDates):
	print stockHistoryData[i,6]
	getAverage[i] = stockHistoryData[i,6]

print "Average is "
print np.mean(getAverage)

#x = np.arange(1500,2500, 50)
#plt.plot(x, getAverage)
"""
"""
for i in getaverage:
	plt.plot()
"""
"""
	print stockHistoryData	[1,1]
	print stockHistoryData.flags
	print stockHistoryData.ndim
	print stockHistoryData.size
	print stockHistoryData.dtype
	print stockHistoryData
	print(len(priceTable))
	print "element are" + str(elementclint/7)
			#stockHistoryData

"""

"""		result = str(price)
		print(result)
		print("Cannot find anything")
"""
