# encoding: utf-8
# @author: MrZhou
# @file: 15字符串.py
# @time: 2023/2/16 10:04
# @desc:
# 创建字符串很简单，只要为变量分配一个值即可
var1 = 'Hello World!'
var2 = "Python Runoob"

# python字符串连接
# print("输出：-", var1[:6] + 'Runoob!')
#
# python转义符
# 需要在字符中使用特殊字符时，python用反斜杠\转义字符
# \n  换行
# \t 横向制表符
# \r 回车
# \\ 反斜杠符号
# \b 退格 backspace
# \f 换页

# python字符串运算符
# a = "Hello"
# b = "Python"
# + 字符串连接
# * 重复输出字符串
# []通过索引获取字符串中字符
# in 成员运算符 如果字符串中包含给定的字符返回True
# % 格式化字符串
# r/R 原始字符串 所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符


print(r'\n')
print(R'\n')

# python字符串格式化，使用C中sprintf函数一样的语法
print("My name is  %s and weight is %d kg!" % ('zara', 21))

%c 格式化字符及其ASCII码
%s 格式化字符串
%d 格式化整数
%f 格式化浮点数字，可指定小数点后的精度
%o 格式化无符号八进制数
%x 格式化无符号十六进制数

# python2.6开始，新增了一种格式化字符串的函数str,format(),它增强了字符串格式化的功能
#
# python三引号允许一个字符串跨多行，字符串中可以包含换行符，制表符及其其他特殊字符
#
# python字符串内建函数 字符串方法是从python1.6到2.0慢慢加进来的
# string.capitalize 把字符串的第一个字符大写
# string.title 返回"标题化"的string,就是说所有单词都是以大写开始。其余字母均为小写
# string.format()格式化字符串
# string.join(seq)以string作为分隔符，将seq中所有的元素（的字符串表示）合并为一个新的字符串
# string.lower() 转换string中所有大写字符为小写
# string.lstrip() 截掉string左边的空格
# string.upper()转换string中的小写字母为大写

