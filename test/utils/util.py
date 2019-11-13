from functools import reduce


# 实现任意函数组合，使用reduce，从参数func中函数右向左执行
def compose(*func):
    def compose_child(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(compose_child, func, lambda x: x)


# 函数组合，支持两个函数，组合函数从右向左执行
def compose_two(f, g):
    # def fg(x):
    #     f(g(x))
    # return fg
    return lambda x: f(g(x))


# 错误的实现方法，使用reduce实现函数组合，从右向左执行
# def compose_wrong(*args):
#     def func(x):
#         def compose_child(f, g):
#             return g(f(x))
#         return reduce(compose_child, args)
#     return func

