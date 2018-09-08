# encoding: utf-8

# 构建User-Agent 
# User-Agent 是什么?
# 是判断用户是用什么浏览器取访问服务器的.如果不加User-Agent取爬网站,User-Agent: python2.7这类的东西 一眼就能看出是爬虫程序
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36

import urllib2


def send_request():
    # 因为urllib2不能构建请求,只能使用request来构建

    # Request(url, data, headers)
    # url 就是统一资源定位符
    # data 请求的方法
    # headers 请求头内容

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    request = urllib2.Request('http://www.baidu.com/', headers=headers)

    response = urllib2.urlopen(request)

    html = response.read()
    return html


if __name__ == '__main__':
    print send_request()
