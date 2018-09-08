# -*- coding: utf-8 -*-
# @File  : 笔趣阁搜索站内API搜索.py
# @Author: 白天好困
# @time: 18-9-8 下午8:26
import requests
import urllib
import codecs
import sys
# http://www.biquge.com.tw/modules/article/soshu.php?searchkey=+%D5%DA%CC%EC
# GET


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "__cdnuid=84b33e6a31820ed57b731218f9d14a6b; jieqiVisitTime=jieqiArticlesearchTime%3D1536409493",
    "Host": "www.biquge.com.tw",
    "If-None-Match": "1536409023|",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
}

book_name = raw_input('请输入书名')

proxies = {"http": "http://maozhaojun:ntkn0npx@115.28.141.184:16816"}

# 进行转码
book_name = book_name.decode('utf-8')
book_name = book_name.encode('gbk')

data = {
    "searchkey": book_name
}

# 发送请求
response = requests.get('http://www.biquge.com.tw/modules/article/soshu.php?', params=data, headers=headers, proxies=proxies)

with codecs.open('1.txt', 'w') as f:
    f.write(response.content)





