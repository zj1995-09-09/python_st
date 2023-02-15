# encoding: utf-8
# @author: MrZhou
# @file: 循环嵌套.py
# @time: 2023/2/15 16:24
# @desc:
# python语言允许在一个循环体里面嵌入另一个循环
# python for 循环:
#     for iterating_var in sequence:
#         for iterating_var in sequence:
#             statements(s)
#         statements(s)
#
#
# python while 循环嵌套语法
#     while expression:
#         while expression:
#             statement(s)
#         statement(s)

i = 2
while (i < 100):
    j = 2
    while j <= (i / j):
        if not (i % j): break
        j = j + 1
    if j > i / j:
        print(i, " 是素数")
    i = i + 1

print("Good bye!")
