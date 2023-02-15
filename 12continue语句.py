# encoding: utf-8
# @author: MrZhou
# @file: 12continue语句.py
# @time: 2023/2/15 16:56
# @desc:
#  continue语句用来高速python跳过当前循环的剩余语句，然后继续进行下一轮循环
# continue 用在while和for循环中

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值 :', var)
print("Good bye!")
