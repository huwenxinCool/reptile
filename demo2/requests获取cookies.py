# -*- coding: utf-8 -*-
# @File  : requests获取cookies.py
# @Author: 白天好困
# @time: 18-9-8 下午7:59
import requests



headers = {
    "Accept": "text/plain, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "自己的cookies",
    "Host": "www.baidu.com",
    "Referer": "https://www.baidu.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
response = requests.get('http://www.baidu.com/', headers=headers)
cookieJar = response.cookies

# 把cookies转成字典
cookiedict = requests.utils.dict_from_cookiejar(cookieJar)

print cookieJar
print cookiedict