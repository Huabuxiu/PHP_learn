import requests
import re

def getHTMLText(url):
    #try:
        r= requests.get(url,timeout = 30)
        r.encoding = 'utf-8'
        return r.text

def parsePage(ilt,html):
    tit = re.findall(r'\"title\"\:\".*?\"',html)
    price = re.findall(r'\"price\"\:\"[0-9]*\"',html)
    for i in range(len(tit)):
        title = eval(re.split('\:', tit[i])[1])
        pri = eval(re.split('\:', price[i])[1])
        ilt.append([title,pri])
def printGoodsList(ilt):
    for i in range(len(ilt)):
        print(ilt[i])

def main():
    goods = '微单'
    depth = 2
    star_url = 'https://s.taobao.com/search?q='+goods
    infoList = []
    for i in range(depth+1):
        url = star_url + '&s=' + str(i*48)
        html = getHTMLText(url)
        parsePage(infoList,html)
    printGoodsList(infoList)

main()
