# -*- coding: utf-8 -*-
# @File  : 网站自发布的CA证书的爬取.py
# @Author: 白天好困
# @time: 18-9-8 下午4:34

# 如12306网站就是自己写的ca证书

# http://www.12306.cn/mormhweb/
# 虽然http也能请求到12306
# 但是用https就会出错

import urllib2
import ssl

# 忽略ssl证书认证
context = ssl._create_unverified_context()

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
}

request = urllib2.Request("https://www.12306.cn/mormhweb/", headers=headers)

response = urllib2.urlopen(request, context=context)

print response.read()