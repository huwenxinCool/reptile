# -*- coding: utf-8 -*-
# @File  : 保持cookies.py
# @Author: 白天好困
# @time: 18-9-8 下午6:50

import cookielib
import urllib2

file_cookies = "cookies.txt"

# 声明一个MozillaCookieJar对象
cookiejar = cookielib.MozillaCookieJar(file_cookies)

handler = urllib2.HTTPCookieProcessor(cookiejar)

headers = {
    "Accept": "text/plain, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "www.baidu.com",
    "Referer": "https://www.baidu.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

opener = urllib2.build_opener(handler)

request = urllib2.Request('http://www.baidu.com/', headers=headers)

opener.open(request).read()
print cookiejar
# 保存cookies
cookiejar.save()

