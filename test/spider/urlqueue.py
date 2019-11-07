# coding=utf-8


# 类似广度优先的策略爬取url
class UrlManager(object):
    def __init__(self):
        self.new_queue = set()
        self.old_queue = set()

    def add_one_url(self, url):
        if url is None:
            return
        if url not in self.new_queue and url not in self.old_queue:
            self.new_queue.add(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_one_url(url)

    def has_new_url(self):
        return len(self.new_queue) != 0

    def get_url(self):
        # pop() 方法用于随机移除一个元素。
        new_url = self.new_queue.pop()
        self.old_queue.add(new_url)
        return new_url
