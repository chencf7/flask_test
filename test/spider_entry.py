# coding=utf-8
# import os
# import sys

# import time
from urllib import parse
from .spider import urlqueue, htmldownload
from .utils.cst_io import write_str2txt
from .re.re_baidubaike import ReBaidubaike


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
        self.urls.add_one_url('https://baike.baidu.com/item/软件/12053')
        self.urls.add_one_url('https://baike.baidu.com/item/软件/12053')
        self.urls.add_one_url('软件')
        # for ul in self.urls.get_url_queue():
        #     print(ul)
        # return

        while self.urls.has_url():
            try:
                if craw_count < 1:
                    # 获取当前爬取的url
                    current_url = self.urls.get_url()
                    print('current page: ', parse.unquote(current_url))
                    # 抓取当前网页的数据
                    current_page = self.loader.download(current_url)
                    if current_page is not None:
                        # craw_urls = ReBaidubaike.get_next_crawler_urls(current_page)
                        craw_urls = ['软件', 'https://baike.baidu.com/item/软件/12053']
                        self.urls.add_urls(craw_urls)

                        print('当前页面待爬取的url')
                        for cu in craw_urls:
                            print(parse.unquote(cu))
                        print(self.urls.get_size())
                        print('======结束')
                        # write_str2txt(current_page, None)
                        # 解析当前网页的数据，保存需要的内容，并添加新的url到url调度器
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
