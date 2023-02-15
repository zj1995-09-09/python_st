# encoding: utf-8
# @author: MrZhou
# @file: break语句.py
# @time: 2023/2/15 16:40
# @desc:
# break语句，就像在C语言中，打破了最小封闭for或while循环
# 用来终止循环语句，即循环条件没有没有False条件或者序列还没有被完全递归完，也会停止执行循环语句

var = 10
while var > 0:
    print('当前变量值 :', var)
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环
        break

print("Good bye!")
