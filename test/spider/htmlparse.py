# coding=utf-8
"""
三种方式解析网页内容，re，lxml，BeautifulSoup
https://www.cnblogs.com/kainhuck/p/10090448.html
"""
import re
from test.re.config import RE_CONFIG


class HtmlParse(object):
    def __init__(self, _parse_name, content):
        self._parser = RE_CONFIG[_parse_name]
        self.content = content

    def parse(self):
        return self._parser.get_next_crawler_urls(self.content)

    def download_img(self):
        self._parser.download_images(self.content)
        pass
