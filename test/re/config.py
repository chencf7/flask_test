# coding=utf-8
from app_start import constant
from .re_baidubaike import ReBaidubaike

constant.BAIDUBAIKE = 'spider_baidubaike'


RE_CONFIG = {
    constant.BAIDUBAIKE: ReBaidubaike
}
