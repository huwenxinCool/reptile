# -*- coding: utf-8 -*-
# @File  : 有道翻译API接口.py
# @Author: 白天好困
# @time: 18-9-8 下午9:01

# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
# POST

import time
import requests
import urllib

data = {
    "i": raw_input('请输入要翻译的单词'),
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": str(int(time.time() * 1000)),
    # 时间戳
    "sign": "3a31dad7ef7ccec6afc1f99821d1db5a",
    # sign 就是一个加密的
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "typoResult": "True",
}

from_data = urllib.urlencode(data)

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": str(len(from_data)),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/?keyfrom=dict2.index",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    # ajax 请求
}

response = requests.post('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule', data=from_data, headers=headers).json()

print response






