import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getURL(url):
    try:
        html = requests.get(url).text
    except HTTPError as e:
        print(e)
        return None
    return html

def getBsObj(html):
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    except AttributeError as e:
        print(e)
        return None
    return bsObj

def getBsObj_lxml(html):
    try:
        bsObj = BeautifulSoup(html,'lxml')
    except ArithmeticError as e:
        print(e)
        return None
    return bsObj

url = "http://www.pythonscraping.com/exercises/exercise1.html"
http = getURL(url)
if http == None:
    print("Tttp could not be found")
else:
    print(http)

bsObj = getBsObj(http)
if bsObj == None:
    print("bsObj could not be found")
else:
    print(bsObj)
