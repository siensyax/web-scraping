# coding: utf-8
import locale
import numpy as np
import math

# ロケールを設定する
#locale.setlocale(locale.LC_COLLATE,'ja_JP')
#消費税を設定
comsumptiontax = 0.08
def cost_calc(tanka,num):
	kagaku = tanka*num
	#kabucom
	print ("カブコム")
	tesuryo = KabucomCashStock(tanka,num)
	print(tesuryo)
	yakujo_kagaku = Yakujo_calc(kagaku,tesuryo,num,tanka)
	print(yakujo_kagaku)

	#SBi
	print("SBI")
	tesuryo = SBI_CashStock(tanka,num)
	yakujo_kagaku = Yakujo_calc(kagaku,tesuryo,num,tanka)
	print(yakujo_kagaku)

def SBI_CashStock(tanka,num):
	#スタンダートプランを対象に。
	kagaku = tanka * num
	billlist = [100000,200000,500000,1000000,1500000,30000000]
	bill=[139,185,272,487,582921,973]
	for i , v  in enumerate(billlist):
		if kagaku <= v:
			tesuryo = bill[i]
			break
		else:
		 tesuryo = 973
	tesuryo_summary = round(tesuryo * (1 + comsumptiontax))
	return  tesuryo_summary

def KabucomCashStock(tanka,num):


	Kagaku=tanka*num
	StockHoldDiscount = 0.06
	NisaDiscount = 0.03


	#逆から回した方かわいい良いか。変わらないか。
	#kabu com
	billlist=[100000,200000,500000]
	bill=[90,150,250]
	i=0

	while i < len(billlist):
		if Kagaku <= billlist[i]:
			tesuryo = bill[i]
			break
		else:
			#print "above"
			tesuryo= min(Kagaku * 0.0009 + 90 ,3690)
		i=i+1

	#手数料の計算
	tesuryosummary= round(tesuryo*(1-StockHoldDiscount)*(1-NisaDiscount)*(1+comsumptiontax),0)

	return tesuryosummary



def Yakujo_calc(Kagaku,tesuryosummary,num,tanka):
		#約定価額
	YakujoKagaku = round(Kagaku + tesuryosummary,0)

	#約定単価
	YakujoTanka =math.ceil(YakujoKagaku / num)

	#手数料加算後の単価向上
	TankaLoss = YakujoTanka - tanka

	return(tesuryosummary,YakujoKagaku,YakujoTanka,TankaLoss)
	if __name__ == '__main__':
		#表示
		#print ("手数料料:"+str(locale.currency(tesuryosummary)) )
		print ("手数料:"+str(tesuryosummary))
		print("約定価額:"+str(YakujoKagaku))
		print("約定単価:"+str(YakujoTanka))
		print("約定単価アップ:"+str(TankaLoss))

	# ロスカット感覚
	LossCut = [10000,20000,30000,50000,70000,100000]
	i=0
	LostTanka=[0] * len(LossCut)
	while i < len(LossCut):
		LostTanka[i] =round((YakujoKagaku - LossCut[i]) / num ,0)
		if __name__ =='__main__':
			print(str(LossCut[i])+"円ロス:"+str(LostTanka[i]))
		i=i+1

"""

def CreditSrock(Ttanka,Num,YakujoDate,LSType)

信用の手数料計算


コスト
手数料消費税
金利
逆日歩貸株料
権利等手数料
消費税
管理料
消費税



今後のコスト推移
"""
