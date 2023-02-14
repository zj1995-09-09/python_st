# encoding: utf-8
# @author: MrZhou
# @file: 条件语句.py
# @time: 2023/2/14 14:44
# @desc:

if 判断条件:
    执行语句。。。
else:
    执行语句。。。

flag = False
name = 'luren'
if name == 'python':         # 判断变量是否为 python
    flag = True              # 条件成立时设置标志为真
    print 'welcome boss'     # 并输出欢迎信息
else:
    print name               # 条件不成立时输出变量名

由于python并不支持switch语句，所以多个条件判断,只能用elif来实现，如果判断需要多个条件需同时判断时，可以使用or或，表示两个条件
有一个成立时判断条件成功，使用and与时，表示只有两个条件同时成立的情况下，判断条件才成功

简单的语句组
可以在同一行的位置上使用if条件判断语句
var = 100
if (var ==100): print("var100")
print("Good bye!")