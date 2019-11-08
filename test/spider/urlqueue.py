# coding=utf-8
from test.utils.cstqueue import CstQueue


# 广度优先的策略爬取url
# 使用自定义队列实现广度优先爬虫url
class UrlManager(object):
    # 此处s_type可传入，深度\广度两种爬取方法
    def __init__(self, s_type='广度'):
        self.new_queue = CstQueue()
        # 以爬取过的url列表
        self.old_queue = set()

    def add_one_url(self, url):
        if url is None:
            return
        if (not self.new_queue.any(url)) and url not in self.old_queue:
            self.new_queue.in_queue(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_one_url(url)

    def has_url(self):
        return self.new_queue.getsize() != 0

    def get_url(self):
        new_url = self.new_queue.out_queue()
        self.old_queue.add(new_url)
        return new_url

# 使用set实现类广度优先爬虫url调度器
# class UrlManager(object):
#     def __init__(self):
#         self.new_queue = set()
#         self.old_queue = set()
#
#     def add_one_url(self, url):
#         if url is None:
#             return
#         if url not in self.new_queue and url not in self.old_queue:
#             self.new_queue.add(url)
#
#     def add_urls(self, urls):
#         if urls is None or len(urls) == 0:
#             return
#         for url in urls:
#             self.add_one_url(url)
#
#     def has_url(self):
#         return len(self.new_queue) != 0
#
#     def get_url(self):
#         # pop() 方法用于随机移除一个元素。
#         new_url = self.new_queue.pop()
#         self.old_queue.add(new_url)
#         return new_url
