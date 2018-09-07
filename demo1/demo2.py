# encoding: utf-8

import urllib.request
# python3 版本

def send_request():
    
    # 发送请求
    response = urllib.request.urlopen('http://www.baidu.com/')

    # 读取
    html = response.read()

    return html

if __name__ == '__main__':
    print(send_request())



