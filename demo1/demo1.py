# encoding: utf-8
# 设置编码

import urllib2
# urllib2 是python2的版本
# python3 是urllib.request 内容差不多

def send_request():
   # 发送请求 
   # respose 是请求体
   # <addinfourl at 139757389467088 whose fp = <socket._fileobject object at 0x7f1bcf825950>>
   response =  urllib2.urlopen('http://www.baidu.com/')
   
   html = response.read()
   # read()读取
   return html


if __name__ == "__main__":
   html = send_request()
   print html
