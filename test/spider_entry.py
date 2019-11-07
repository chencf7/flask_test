# coding=utf-8
# import os
# import sys
# sys.path.append(os.getcwd())

import time
from .spider import urlqueue, htmldownload
entry_url = 'https://baike.baidu.com/item/github/10145341?fr=aladdin'


class SpiderEntry(object):
    def __init__(self):
        self.urls = urlqueue.UrlManager()
        self.downloader = htmldownload.HtmlPageLoader()

    # 爬虫调度程序
    def dispatch(self, url):
        if url is None:
            return None
        self.urls.add_one_url(url)
        while self.urls.has_new_url():
            try:
                current_url = self.urls.get_url()
            except Exception as err:
                print(err)


if __name__ == '__main__':
    print('开始爬取数据：')
    print('entry url: {}'.format(entry_url))
    _st = time.time()
    print(_st)
    sp = SpiderEntry()
    sp.dispatch()
    pass
