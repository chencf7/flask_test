# coding=utf-8
import requests


class HtmlPageLoader(object):
    def __init__(self):
        # 记录爬取的url个数
        self.count = 0
        pass

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
            return data.text
        return None

    def download_page_count(self):
        return self.count
