# encoding: utf-8
# @author: MrZhou
# @file: 13pass语句.py
# @time: 2023/2/15 17:20
# @desc:

# pass是空语句为了保持程序结构的完整性
# pass不做任何事情，一般用做占位语句

for letter in 'python':
    if letter == 'h':
        pass
        print('这是pass块')
    print('当前字母:', letter)
print("Good bye")
