# encoding: utf-8
# @author: MrZhou
# @file: 36 PythonJSON.py
# @time: 2023/2/22 16:10
# @desc:


# json JavaScript Object Notations是一种轻量级的数据交换格式
# import json
#
# json.dumps()将python对象编码成Json字符串
# json.loads()将已编码的JSON字符串解码成为python对象


# 关于load()和dump()的区别：
# loads： 是将 string 转换为 dict
# dumps： 是将 dict 转换为 string
# load： 是将 json格式字符串转化为 dict，读取文件
# dump： 是将 dict类型转换为 json格式字符串，存入文件


dump 和 dumps 都实现了序列化
load 和 loads 都实现反序列化
变量从内存中变成可存储或传输的过程称之为序列化
序列化是将对象状态转化为可保存或可传输格式的过程。

变量内容从序列化的对象重新读到内存里称之为反序列化
反序列化是流转换为对象。

import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

data2 = json.dumps(data)
print(data2)
# [{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]

python 原始类型向 json 类型的转化对照表：

Python	JSON
dict	object
list, tuple	array
str, unicode	string
int, long, float	number
True	true
False	false
None	null