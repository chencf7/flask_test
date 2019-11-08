# coding=utf-8


class CstQueue(object):
    def __init__(self, size=100):
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

    def any(self, element):
        exits_arr = filter(lambda itm: itm == element, self.queue)
        return len(list(exits_arr)) > 0

    def empty(self):
        self.queue = []
        self.end = -1

