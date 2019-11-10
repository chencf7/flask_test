# coding=utf-8
import time
from flask import Flask, render_template
from test.spider_entry import SpiderEntry
from test.re_entry import re_test

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    # app.debug = True
    # app.run(host='127.0.0.1', port=5011, debug=True)

    # entry_url = 'https://baike.baidu.com/item/github/10145341?fr=aladdin'
    entry_url = 'https://bbs.hupu.com/30452896.html'

    # print('开始爬取数据：')
    # print('entry url: {}'.format(entry_url))
    # _st = time.time()
    spe = SpiderEntry()
    spe.dispatch(entry_url)

    # re_test()
