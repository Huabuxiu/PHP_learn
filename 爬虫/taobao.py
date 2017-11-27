import requests
import re

def getHTMLText(url):
    try:
        r= requests.get(url,timeout = 30)
        r.rasise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

def parsePage(ilt,html):
    print("")

