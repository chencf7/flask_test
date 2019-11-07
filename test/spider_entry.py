# coding=utf-8
# import os
# import sys
# sys.path.append(os.getcwd())

import time
from .spider import urlqueue, htmldownload


class SpiderEntry(object):
    def __init__(self):
        self.urls = urlqueue.UrlManager()
        self.downloader = htmldownload.HtmlPageLoader()

    # 爬虫调度程序，深度爬取/广度爬取
    def dispatch(self, url):
        # print(url)
        if url is None:
            return None
        self.urls.add_one_url(url)
        while self.urls.has_url():
            try:
                current_url = self.urls.get_url()
            except Exception as err:
                print(err)


if __name__ == '__main__':
    # 直接执行报错，引入错误，到venv根目录的hello.py执行
    sp = SpiderEntry()
    sp.dispatch()
    pass
