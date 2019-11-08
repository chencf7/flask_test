# coding=utf-8
"""
学习re，正则表达式验证的各种使用方式
match 匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。
search 在string 中进行搜索，成功返回Match object, 失败返回None, 只匹配一个
findall 在string 中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象
finditer 在string 中查找所有 匹配成功的字符串, 返回iterator，每个item是一个Match object
sub 替换
"""

import re
from .utils.cst_io import read_txt, write_str2txt
from .re.common import ReUtil

# r''，代表字符串为raw string
reg_test = r'<html>'
# 匹配脚本文件正则
regex_script = r'<script(?:>| type| src| async)[\s\S]*?</script>'
regex_style = r'<style(?:>| type)[\s\S]*?</style>'

reg_title = r'<title>.*?</title>'
reg_desp_kw = r'<meta name="(?:description|keywords).*?>'

reg_baike_item = r'<a.*?href="/item/.*?</a>'


def re_test():
    result = read_txt('tmp')
    # print(result)

    # exact_str = re.sub(regex_script, r'', result)
    # write_str2txt(exact_str, None)
    # 获取网页标题
    str_title = re.search(reg_title, result)
    print(ReUtil.clear_tag(str_title.group(0)))

    str_desp_kw = re.findall(reg_desp_kw, result)
    for dk in str_desp_kw:
        print(dk)

    new_urls = re.findall(reg_baike_item, result)
    for url in new_urls:
        print(url)
    pass


if __name__ == '__main__':
    re_test()
