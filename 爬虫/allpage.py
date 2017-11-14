from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html)
	for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:		#attrs['href']返回一个字典
				#遇到新页面
				newPage = link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getlinks(newPage)

getlinks("")