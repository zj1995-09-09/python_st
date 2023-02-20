# encoding: utf-8
# @author: MrZhou
# @file: 18字典Dictionary.py
# @time: 2023/2/16 14:48
# @desc:

# 字典是另一种可变容器模型，且可存储任意类型对象

# d = {key1: value1, key2: value2}
#
# import keyword
#
# print(keyword.kwlist)

# dict作为python的关键字和内置函数，变量名不建议命名为dict
#
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
#
# 访问字典里的值 把相应的键放入熟悉的方括弧
#
# 如果字典里没有的键访问数据，会输出错误如下
# KeyError:
#
# 修改字典，向字典添加新内容的方法是增加新的键值对，修改或删除已有键值对

# 删除字典元素
# 删除单一的元素也能清空字典，清空只需一项操作
#
# tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
# del tinydict['Name']  # 删除键是'Name'的条目
# tinydict.clear()  # 清空字典所有条目
# del tinydict  # 删除字典
#
# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
tinydict = {['Name']: 'Zara', 'Age': 7}

print("tinydict['Name']: ", tinydict['Name'])
TypeError: unhashable type: 'list'

字典内置函数&方法
cmp(dict1,dict2)比较两个字典元素
len(dict)计算字典元素个数，即键的总数
str(dict)输出字典可打印的字符串表示
type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型

内置方法
dict.clear()删除字典内的所有元素
dict.copy()返回一个字典的浅复制
dict.items()以列表返回可遍历的(键，值)元组数组
dict.keys()以列表返回一个字典的所有键
dict.values()以列表返回字典中的所有值
popitem() 返回并删除字典中的最后一对键和值