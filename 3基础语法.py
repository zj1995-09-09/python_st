# encoding: utf-8
# @author: MrZhou
# @file: 3基础语法.py
# @time: 2023/2/13 19:15
# @desc:
# 控制台作用:相当于在当前目录 (当前所打开的文件所在的目录) 下打开python解释器，
# 就相当于直接在cmd中输入python后的运行环境-
# 终端作用:相当于在当前且录真接打开cmd

print("Hello,Python!")

# python 2.X中使用python 3.X的print函数
# 可以导入_future_包，该包禁用python2.X的print 语句，采用python 3.x的print函数
#
# python标识符，由字母、数字、下划线组成，不能以数字开头
# 标识符区分大小写
# 以下划线开头的标识符是有特殊意义的，以单下划线开头_foo的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用from xxx ,import *导入
# 以双下划线开头的__foo代表类的私有成员，以双下划线开头和结尾的__foo__代表python里特殊方法专用的标识，如__init__()代表类的构造函数
# python可以同一行显示多条语句，方法是用分号；分开 如
print('hello');
print('runoob');

# python 保留关键字 不能用作常数或变数，或任何其他标识符名称
# 所有python关键字只包含小写字母

import keyword

print(keyword.kwlist)

# 多行语句 \
total = item_one + \
        item_two + \
        item_three

python
引号 ‘ 双引号
""
三引号
""" """
来表示字符串，引号的开始与结束必须是相同类型的
其中三引号
""""""
由多行组成，组成多行文本的快捷语法，常用于文档字符串，在文件的特地地点被当做注释
word = 'word'
sentence = "这是一个句子"
paragraph = """ 这是一个段落
包含了多个语句"""

python
注释
采用  # 开头
# 第一个注释
print("Hello,Python!")  # 第二个注释

# python多行注释使用三个单引号
# '''   '''
# 或者三个双引号
# """

python 空行 函数之间或类的方法之间用空行分隔，表示一段新的代码开始，类和函数入口之间也用一行空行分隔，以突出函数入口的开始
空行与代码缩进不一样，作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构
记住：空行也是程序代码的一部分

等待用户输入
raw_input(“按下enter键退出，print(其他任意键显示...\n )
\n 代表换行，一旦用户按下enter键退出，其他键显示。


print默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号，
x = "a"
y = "b"
#换行输出
print(x)
print(y)
print("_____")

#不换行输出
print(x),
print(y),

#不换行输出
print(x,y)

缩进相同的一组语句构成一个代码块，我们称之为代码组

很多程序可以执行一些操作来查看一些基本信息，python可以使用-h来查看各参数帮助信息