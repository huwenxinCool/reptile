# -*- coding: utf-8 -*-
# @File  : requests模拟登录.py
# @Author: 白天好困
# @time: 18-9-8 下午8:03
import requests


cookies_dict = '登录的cookies'

headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
}

headers['Cookie'] = requests.utils.cookiejar_from_dict(cookies_dict)

response = requests.get('http://www.baidu.com/', headers=headers)
print response.content
