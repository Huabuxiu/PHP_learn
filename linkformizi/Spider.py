from  urllib.request import urlopen
import urllib.request
import urllib
import requests
from bs4 import BeautifulSoup
import time
import json

def save(srclink):
    res = requests.get(srclink)
    with open(str(time.time()) + ".jpg", 'wb') as f:
        f.write(res.content)


def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    url = urllib.request.Request(url=url, headers=headers)
    html = urlopen(url)
    bsObj =  BeautifulSoup(html)
    links = bsObj.findAll('img')
    for link in links:
         srclink = link["src"]
         save(srclink)



url = 'https://www.eee668.com/htm/girl7/2057.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url = urllib.request.Request(url=url, headers=headers)
html1 = urlopen(url)
bsobj = BeautifulSoup(html1)
links = bsobj.find("ul",{"class":"movieList"})
print(links)
# for link in links:
# pagelink = links[0]
# pagelink = "https://www.eee686.com"+pagelink.attrs['href']
# url = urllib.request.Request(url=pagelink, headers=headers)
# html1 = urlopen(url)
# = html1.getcode()
    # pagelink = urllib.request.Request(url=pagelink, headers=headers)
    # html1 = urlopen(url)
    # bsobj = BeautifulSoup(html1)
    # links = bsobj.findAll('img')
    # for link in links:
    #     srclink = link["src"]
    #     save(srclink)
    # get_page(pagelink)