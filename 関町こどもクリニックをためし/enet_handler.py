# -*- encoding: utf-8 -*-
# 文字コードの設定
# インポートする
import re
import mechanize
from bs4 import BeautifulSoup

# urllib2
# beautifulsoup

# インスタンス作成
br = mechanize.Browser()

# 非ロボット化（これは何？）
br.set_handle_robots('false')

# 1)トップ画面から診察受付へ
# まずは、診察受付のURLを開く

response = br.open("http://euke.jp/enet/do/usr/entry/select/top?ID=72")

response.get_data()
print("nyaa")  # 検証用
source = str(response.get_data())

# セッションIDをGETする。
# logo_bg を探す
# そこに入っているリンク先URLをGETする。
# そこから正規表現で、jsessionid=から?ID=までをGETする。
# イメージ：<a href="/enet/do/usr/search/hospital;jsessionid=B6A7A0120B778A559732121CE9B4C33F?ID=72">
# beautifulsoupにHTMLソースを渡す
print(source)
soup = BeautifulSoup(source, "html.parser")
# セッションIDのありかをゲットする
# assert isinstance(soup.find("img", name="entry").previous_sibling,object )

SessionIdInclText = soup.find_all("td", attrs={"class": "logo_bg"})

print(SessionIdInclText)

# 正規表現あるいはBeautifulsoupの関数でセッションIDをGETして、変数に格納する。正規表現はやめ。Puthonネイティヴの文字列ハンドリングでゲット。
# まずは、jsessionidの位置をゲット
#後でキーレングスを使うので、キーは変数に入れておく。
SessionIdKey = "jsessionid="
#スタートの位置をゲット
SessionIdStartColumn = str(SessionIdInclText).find(SessionIdKey)
print(SessionIdStartColumn)
#エンドの位置をゲット
SessionIdEndColumn = str(SessionIdInclText).find("?ID")
print(SessionIdEndColumn)
#スライスでゲットする
SessionId = str(SessionIdInclText)[int(SessionIdStartColumn)+len(SessionIdKey):int(SessionIdEndColumn)]
print(SessionId)
#print(response)

# 次に、リンクを開いてみる。

br.open("http://euke.jp/enet/do/usr/entry/select/top?ID=72")
# br.page.link_withs(:src => "/enet/do/usr/entry/select/top?ID=72")[0].click

#br.page.link_with( :text=>"オークション").click


# 2)フォームをサブミット
# 今回は不要：外部ファイルからIDとパスワードをGETする
# FORMをセレクト

# FORMに入力する

# SUBMITする

# SUBMITの結果をレスポンスで受け取る

# 次の画面
