# encoding: utf-8
# @author: MrZhou
# @file: 26内置函数.py
# @time: 2023/2/20 19:08
# @desc:

# abs()返回数字的绝对值
#
# enumerate(sequence,[start=0]) 返回enumerate(枚举)对象
# sequence 一个序列、迭代器或其他支持迭代对象
# start-下标起始位置的值

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# a = list(enumerate(seasons, start=1))  # 下标从 1 开始
# print(a)


# for循环使用enumerate
# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
#     print(i, element)
#
#
# python eval()函数
# 用来执行一个字符串表达式 并返回表达式的值
# n =81
# eval("n+4")
# 85

# zip()用于将可迭代的对象作为参数，将对象中对象的元素打包成一个个元组
# 然后返回由这些元组组成的列表
# zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。


# super()
#
#
# class A:
#     def add(self, x):
#         y = x + 1
#         print(y)
#
#
# class B(A):
#     def add(self, x):
#         super().add(x)
#
#
# b = B()
# b.add(2)  # 3

# pow() 方法返回 xy（x 的 y 次方） 的值。
# import math
# math.pow(x,y)
#
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

# getattr()
# >>>class A(object):
# ...     bar = 1
# ...
# >>> a = A()
# >>> getattr(a, 'bar')        # 获取属性 bar 值
# 1
# >>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'A' object has no attribute 'bar2'
# >>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
# 3


cmp()