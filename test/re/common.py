# coding=utf-8
import re


class ReUtil(object):
    # 匹配脚本文件正则
    regex_script = r'<script(?:>| type| src| async)[\s\S]*?</script>'
    regex_style = r'<style(?:>| type)[\s\S]*?</style>'

    # 匹配2个以上换行符
    reg_linefeed = r'(\r\n){2,}|\n{2,}'

    reg_tag = r'<.*?>'

    @staticmethod
    # 删除不必要的下载网页的元素
    # 删除脚本内容 <script> <style>
    def exact_script_style(data):
        no_script_text = re.sub(ReUtil.regex_script, r'\n', data)
        no_style_text = re.sub(ReUtil.regex_style, r'\n', no_script_text)
        return no_style_text

    @staticmethod
    # 匹配连续2个以上的换行符、回车符，并替换为一个
    def exact_linefeed(data):
        return re.sub(ReUtil.reg_linefeed, r'\n', data)

    @staticmethod
    def clear_tag(_str):
        return re.sub(ReUtil.reg_tag, r'', _str)
