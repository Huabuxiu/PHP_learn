#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# 爬取目标
url = 'http://www.mzitu.com/page/'
# 设置报头，Http协议
header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
# 爬取的预览页面数量
preview_page_cnt = 2
for cur_page in range(1, int(preview_page_cnt)+1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers = header)
    # 解析网页
    soup = BeautifulSoup(cur_page.text, 'html.parser')
    # 图片入口和文字入口取一个即可
    preview_link_list = soup.find(id='pins').find_all('a', target='_blank')[1::2]
    for link in preview_link_list:
        print(link)