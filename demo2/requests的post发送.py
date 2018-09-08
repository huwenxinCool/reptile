# -*- coding: utf-8 -*-
# @File  : requests的post发送.py
# @Author: 白天好困
# @time: 18-9-8 下午7:25

import requests
import time
import urllib

input_str = raw_input('请输入要翻译的内容')

data = {
    "source": "auto",  # 根据系统的来判断的
    "target": "en",  # 要转换车成的语言
    "sourceText": input_str,  # 这个为查询的值
    "sessionUuid": "translate_uuid" + str(int(time.time() * 1000))  # 这个为时间戳
}
from_data = urllib.urlencode(data)
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate", 这个是指压缩格式
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": str(len(from_data)),  # 这个是指请求的表单的长度
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "fanyi.qq.com",
    "Origin": "https://fanyi.qq.com",
    "Referer": "https://fanyi.qq.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"  # 这个就是AJAX请求
}

# headers = urllib.urlencode(headers)

result = requests.post('https://fanyi.qq.com/api/translate', data=from_data, headers=headers).json()
# 注意 这里的headers不能为int类型
# data 可以为字典或者urlencode编码的 headers就不可以了  只能为字典类型

print result["translate"]["records"][0]["targetText"]

# print result['translate']['records'][0]['targetText']
