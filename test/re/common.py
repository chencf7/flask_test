# coding=utf-8
import re


class ReUtil(object):
    reg_tag = r'<.*?>'

    @staticmethod
    def clear_tag(_str):
        return re.sub(ReUtil.reg_tag, r'', _str)
