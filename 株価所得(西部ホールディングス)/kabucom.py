# coding: utf-8
import  locale
import numpy as np

# ロケールを設定する
#locale.setlocale(locale.LC_COLLATE,'ja_JP')

def CashStock(tanka,num):


	Kagaku=tanka*num
	comsumptiontax = 0.08
	StockHoldDiscount = 0.06
	NisaDiscount = 0.03

	#逆から回した方かわいい良いか。変わらないか。

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

	#約定価額
	YakujoKagaku = round(Kagaku + tesuryosummary,0)

	#約定単価
	YakujoTanka =round(YakujoKagaku / num ,0)

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
