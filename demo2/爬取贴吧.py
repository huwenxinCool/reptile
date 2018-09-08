# -*- coding: utf-8 -*-
# @File  : 爬取贴吧.py
# @Author: 白天好困
# @time: 18-9-8 下午9:33

# https://tieba.baidu.com/f?kw=lol&pn=50
import requests


class tieba(object):
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?'
        self.name = raw_input('请输入要爬取的贴吧名字')
        self.page = int(raw_input('请输入要爬取的页数'))
        self.file_name = self.name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }

    def send_request(self, page):
        data = {
            "kw": self.name,
            "pn": (page - 1) * 50
        }
        print "[INFO] : 正在爬取第{}页".format(page)
        response = requests.get(self.url, params=data, headers=self.headers)
        self.save(response, page)

    def save(self, response, page):
        with open(self.name + str(page) + '.html', 'w') as f:
            f.write(response.content)
            print "[INFO] : 正在写入第{}页".format(page)

    def start(self):
        for i in range(1, self.page + 1):
            # 开启爬取
            self.send_request(i)


if __name__ == '__main__':
    t = tieba()
    t.start()
