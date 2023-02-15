# encoding: utf-8
# @author: MrZhou
# @file: for 7循环语句.py
# @time: 2023/2/15 10:40
# @desc:
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串
#
# for iterating_var in sequence:
#     statement(s)

# for letter in 'Python':  # 第一个实例
#     print("当前字母: %s" % letter)
#
# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:  # 第二个实例
#     print('当前水果: %s' % fruit)
#
# print("Good bye!")
#
# 通过序列索引迭代

# fruits = ['banana', 'apple', 'mango']
#
# for index in range(len(fruits)):
#     print('当前水果 : %s' % fruits[index])
#
# print("Good bye!")
#
#
# 循环使用else语句

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('{}等于{}*{}'.format(num, i, j))
            break
    else:
            print("{}是一个质数".format(num))
