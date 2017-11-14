import requests

def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text[:1000]
	except:
		return "产生异常"

if __name__ == "__main__":
	url = "https://item.jd.com/3989389.html#crumb-wrap"
	print(getHTMLText(url))