# -*- coding: utf-8 -*-
# @File  : demo5.py
# @Author: 白天好困
# @time: 18-9-7 下午5:57

import urllib2
import urllib


# https://tieba.baidu.com/f?kw=lol&pn=50





def send_reequest(str_dict):

    str_url = urllib.urlencode(str_dict)

    url = 'https://tieba.baidu.com/f?' + str_url

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    request = urllib2.Request(url, headers=headers)

    response = urllib2.urlopen(request).read()

    with open('text.html', 'a') as f:
        f.write(response)


def send_request_page(str_dict, page):

    i = 1

    while i <= int(page):

        str_dict['pn'] = (i-1) * 50
        send_reequest(str_dict)
        print "第%d页爬取完毕" % i
        i += 1



if __name__ == '__main__':
    str = raw_input('请输入要爬取的贴吧')
    page = raw_input('请输入要爬去的页数')

    str_dict = {
        'kw': str
    }

    send_request_page(str_dict, page)
