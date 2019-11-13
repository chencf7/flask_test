# coding=utf-8
import sys


class _const(object):
    class ConstError(PermissionError):
        pass

    class ConstCaseError(ConstError):
        pass

    # 重写__setarr__方法
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError('Cannot change const {}'.format(key))
        if not key.isupper():
            raise self.ConstCaseError('Const name {} is not all uppercase'.format(key))
        self.__dict__[key] = value


# 将系统加载的模块列表中的 constant 替换为 _const() 实例
sys.modules[__name__] = _const()
