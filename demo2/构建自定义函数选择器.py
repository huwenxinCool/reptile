# -*- coding: utf-8 -*-
# @File  : 构建自定义函数选择器.py
# @Author: 白天好困
# @time: 18-9-8 下午4:24

# proxyHandler 处理器
# 代理处理

import urllib2

# http://httpbin.org/p
# proxy = {"http" : "http://maozhaojun:ntkn0npx@115.28.141.184:16816"}
proxy = {}
# 构建自定义的处理器
httpHandler_proxy = urllib2.ProxyHandler(proxy)

request = urllib2.Request('http://httpbin.org/ip')

opener = urllib2.build_opener(httpHandler_proxy)

print opener.open(request).read()
