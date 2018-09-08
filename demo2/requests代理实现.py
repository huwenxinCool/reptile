# -*- coding: utf-8 -*-
# @File  : requests代理实现.py
# @Author: 白天好困
# @time: 18-9-8 下午7:52

import requests

proxy = {"http" : "http://username:password@ip:port"}

html = requests.get('http://httpbin.org/ip', proxies=proxy)
# proxies 接收一个字典来实现代理
print html.content
