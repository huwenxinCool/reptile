# -*- coding: utf-8 -*-
# @File  : 豆瓣电影.py
# @Author: 白天好困
# @time: 18-9-8 下午3:16

import urllib2
import urllib
import json
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20


headers = {
    "Host": "movie.douban.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Referer": "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=",
    #"Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8"
}

def send_request(num_dict):

    base_url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&"
    # type 为类型
    # start 从什么地方开始

    full_url = base_url + urllib.urlencode(num_dict)

    # 构建请求
    request = urllib2.Request(full_url, headers=headers)

    # 发送请求
    response = urllib2.urlopen(request).read()
    html_str = json.loads(response)
    for i in range(0, len(html_str)):
        print html_str[i]['title']



num = int(raw_input('请输入要查询多少数据'))

num_dict = {
    "limit": num
}

send_request(num_dict)