# coding=utf-8
# import os
# import sys

# import time
from .spider import urlqueue, htmldownload
from .utils.cst_io import write_str2txt


class SpiderEntry(object):
    def __init__(self):
        self.urls = urlqueue.UrlManager()
        self.loader = htmldownload.HtmlPageLoader()

    # 爬虫调度程序，深度爬取/广度爬取
    def dispatch(self, url):
        if url is None:
            return None
        self.urls.add_one_url(url)
        while self.urls.has_url():
            try:
                # 获取当前爬取的url
                current_url = self.urls.get_url()
                # 抓取当前网页的数据
                current_page = self.loader.download(current_url)
                # print(current_page)
                write_str2txt(current_page, None)
                # 解析当前网页的数据，保存需要的内容，并添加新的url到url调度器
            except Exception as err:
                print(err)


if __name__ == '__main__':
    # 直接执行报错，引入错误，到venv根目录的hello.py执行
    sp = SpiderEntry()
    sp.dispatch()
    pass
