# -*- coding: utf-8 -*-
# @File  : requests处理ssl安全的问题.py
# @Author: 白天好困
# @time: 18-9-8 下午8:12
import requests

response = requests.get('https://www.12306.cn/mormhweb/', verify=False)
# verify默认为True  就是开启的
# 把它修改为False就关闭就可以处理了

print response.content
