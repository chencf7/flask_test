# coding=utf-8


class CstStack(object):
    def __init__(self):
        self.stack = []

    def push(self, itm):
        self.stack.append(itm)

    def pop(self):
        # 数组pop方法删除并返回数组最后一个元素
        itm = self.stack.pop()
        return itm

    def clear(self):
        del self.stack

    def is_empty(self):
        return len(self.stack) == 0

    def getsize(self):
        return len(self.stack)
