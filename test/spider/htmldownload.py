# coding=utf-8
import requests

from test.re.common import ReUtil


# def exact_file():
#     yield ReUtil.exact_script_style()
#     yield ReUtil.exact_linefeed()

# 函数组合，支持两个函数，组合函数从右向左执行
def compose_two(f, g):
    # def fg(x):
    #     f(g(x))
    # return fg
    return lambda x: f(g(x))


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

        try:
            sessions = requests.session()
            sessions.headers = headers
            data = sessions.get(url)
            if data.status_code == 200:
                data.encoding = 'utf-8'
                # 删除不必要的下载网页的元素
                # 组合函数从右向左执行
                exact_fun = compose_two(ReUtil.exact_linefeed, ReUtil.exact_script_style)
                return exact_fun(data.text)
                # return ReUtil.exact_linefeed(ReUtil.exact_script_style(data.text))
            # 判断request下载网页是否成功，否返回None
            return None
        except Exception as err:
            return None

    def download_page_count(self):
        return self.count
