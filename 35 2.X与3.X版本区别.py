# encoding: utf-8
# @author: MrZhou
# @file: 35 2.X与3.X版本区别.py
# @time: 2023/2/22 15:13
# @desc:

# python3.0版本称为python3000，简称Py3k，相对于Python的早期版本，这是一个较大的升级
#
# 为了不带入过多的累赘，python3.0在设计的时候没有考虑向下相容
#
# print 函数
# print 语句没有了，取而代之的是 print() 函数。 Python 2.6 与 Python 2.7 部分地支持这种形式的 print 语法。在 Python 2.6 与Python 2.7 里面，以下三种形式是等价的：
#
# 如果 Python2.x 版本想使用使用 Python3.x 的 print 函数，可以导入 __future__ 包，该包禁用 Python2.x 的 print 语句，采用 Python3.x 的 print 函数
# # from __future__ import print_function

# Python3.x 与 Python2.x 的许多兼容性设计的功能可以通过 __future__ 这个包来导入。
#
# python2有ASCII str()类型，Unicod()是单独的 不是byte类型
# 现在python3 ，最终有了Unicode(utf-8)字符串，以及一个字节类：byte和bytearrays
#
# 由于python3.X源码文件默认使用utf-8编码，所以使用中文就更加方便了
#
# 异常
# python3处理异常也轻微的改变了，在python3中现在使用as作为关键词
# 捕获异常的语法由 except exc, var 改为 except exc as var
# 使用语法except (exc1, exc2) as var 可以同时捕获多种类别的异常。 Python 2.6 已经支持这两种语法。
#
# 不等运算符
# Python 2.x中不等于有两种写法 != 和 <>
#
# Python 3.x中去掉了<>, 只有!=一种写法，还好，我从来没有使用<>的习惯

数据类型
1）Py3.X去除了long类型，现在只有一种整型——int，但它的行为就像2.X版本的long

2）新增了bytes类型，对应于2.X版本的八位串，定义一个bytes字面量的方法如下：
b =b'china'

#
# str对象和bytes对象可以使用.encode(str -> bytes)或.decode(bytes -> str)方法相互转化
#
# bytes-str
# s=b.decode()
# s
# 'china'
#
# str-bytes
# b1=s.encode()
# b1
# b'china'



