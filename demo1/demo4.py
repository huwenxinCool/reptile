# -*- coding: utf-8 -*-
# @File  : demo4.py
# @Author: 白天好困
# @time: 18-9-7 下午5:48

import urllib2
import urllib

def send_request(wd):
    # https://www.baidu.com/s?wd=%E9%BB%91%E9%A9%AC%E7%A8%8B%E5%BA%8F%E5%91%98
    # 把中文转成urlencode格式
    wd = urllib.urlencode(wd)
    # 设置请求url 拼接
    url = 'https://www.baidu.com/s?' + wd

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    # 发送请求
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()

if __name__ == '__main__':
    kw = raw_input('请输入要搜索的关键字')
    wd = {"wd": kw}
    print send_request(wd)

