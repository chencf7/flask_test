# coding=utf-8
import operator


class CstQueue(object):
    def __init__(self, size=999):
        self.queue = []
        self.size = size
        self.end = -1

    def set_total_size(self, size):
        self.size = size

    def getsize(self):
        return len(self.queue)

    def in_queue(self, element):
        if self.end < self.size-1:
            self.queue.append(element)
            self.end += 1
        else:
            raise Exception('Queue is Full')

    def out_queue(self):
        if self.end != -1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end -= 1
            return element
        else:
            raise Exception('Queue is empty')

    def get_queue(self):
        return self.queue

    def has(self, element):
        # flag = False
        # for itm in self.queue:
        #     if itm == element:
        #         flag = True
        # return flag

        def compare_two(t1):
            return t1 == element

        exits_arr = filter(compare_two, self.queue)
        # exits_arr = filter(lambda itm: itm == element, self.queue)
        # exits_arr = filter(lambda itm: itm.strip() == element.strip(), self.queue)
        # exits_arr = filter(lambda itm: operator.eq(itm, element), self.queue)
        return len(list(exits_arr)) > 0

    def empty(self):
        self.queue = []
        self.end = -1

