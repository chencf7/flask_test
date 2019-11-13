# coding=utf-8
# import os
# import sys

# import time
from urllib import parse
from .spider import urlqueue, htmldownload, htmlparse
from .utils.cst_io import write_str2txt
from .re.config import constant


class SpiderEntry(object):
    def __init__(self):
        self.urls = urlqueue.UrlManager()
        self.loader = htmldownload.HtmlPageLoader()

    # 爬虫调度程序，深度爬取/广度爬取
    def dispatch(self, url):
        if url is None:
            return None
        craw_count = 0
        self.urls.add_one_url(url)

        while self.urls.has_url():
            try:
                if craw_count < 2:
                    # 获取当前爬取的url
                    current_url = self.urls.get_url()
                    # print('current page: ', parse.unquote(current_url))
                    # 抓取当前网页的数据
                    page_content = self.loader.download(current_url)
                    if page_content is not None:
                        # 解析当前网页的数据
                        # 1，添加新的url到url调度器
                        # 2，获取数据
                        # 3，下载图片
                        _parser = htmlparse.HtmlParse(constant.BAIDUBAIKE, page_content)
                        craw_urls = _parser.parse()
                        self.urls.add_urls(craw_urls)

                        _parser.download_img()
                        for cu in self.urls.get_url_queue():
                            print(parse.unquote(cu))
                        # print(self.urls.get_size())

                        # write_str2txt(current_page, None)

                        craw_count += 1
                else:
                    break
            except Exception as err:
                print(err)


if __name__ == '__main__':
    # 直接执行报错，引入错误，到venv根目录的hello.py执行
    sp = SpiderEntry()
    sp.dispatch()
    pass
