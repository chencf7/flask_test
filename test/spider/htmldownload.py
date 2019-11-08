# coding=utf-8
import requests
import re

# 匹配脚本文件正则
regex_script = r'<script(?:>| type| src| async)[\s\S]*?</script>'
regex_style = r'<style(?:>| type)[\s\S]*?</style>'


class HtmlPageLoader(object):
    def __init__(self):
        # 记录爬取的url个数
        self.count = 0
        pass

    # 精简不必要的下载网页的元素
    # 1. 删除脚本内容 <script>
    def __exact(self, data):
        no_script_text = re.sub(regex_script, r'', data)
        no_style_text = re.sub(regex_style, r'', no_script_text)
        return no_style_text

    def download(self, url):
        if url is None:
            return None
        self.count += 1
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/77.0.3865.90 Safari/537.36 '
        headers = {'User_Agent': user_agent}

        sessions = requests.session()
        sessions.headers = headers
        data = sessions.get(url)
        if data.status_code == 200:
            data.encoding = 'utf-8'
            return self.__exact(data.text)
        return None

    def download_page_count(self):
        return self.count
