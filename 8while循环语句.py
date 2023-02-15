# encoding: utf-8
# @author: MrZhou
# @file: 8while循环语句.py
# @time: 2023/2/14 16:35
# @desc:


# while  判断条件(condition):
#     执行语句(statements).....


# count = 0
# while count < 9:
#     print('the count is:', count)
#     count += 1
#
# print('Good bye')
#
#
# while  语句还有另外两个重要的命令continue，break 跳过循环
# 循环使用else语句
# count = 0
# while count < 5:
#     print(count, 'is less than 5')
#     count += 1
# else:
#     print(count, 'is not less than 5')
#
# 简单语句组
# 类似if语句语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
flag = 1
while flag: print('Given flag is really true')
print("Good bye")
