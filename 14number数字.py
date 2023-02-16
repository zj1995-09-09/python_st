# encoding: utf-8
# @author: MrZhou
# @file: 14number数字.py
# @time: 2023/2/15 17:26
# @desc:

# python数字类型用于存储数值
# 数据类型是不允许改变的，如果改变number数据类型的值，将重新分配内存空间
# var1=1
# var2=10
#
# del var1,var2
# 四种不同的数值类型
# int 整型或整数，正负不带小数点
# long integer 无限大小的整数，整数最后是一个大写或小写的L
# floating point real values 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示 2.5e2 = 2.5 x 102 = 250
# complex 复数由实数部分和虚数部分构成，可以用a+bj,或者complex(a,bd)表示，复数的实部a和虚部b都是浮点型
#
# int	long	float	complex
# 10	51924361L	0.0	3.14j
#
# python math cmath
# math提供了许多对浮点数的数学运算函数
# python cmath 包含了一些用于复数运算的函数
#
# 要使用math 或cmath函数必须先导入
import math

print(dir(math))

python 随机函数
choice(seq) 从序列的元素中随机挑选一个元素，比如random.choice(range(10)),从0到9中随机挑选一个整数

python三角函数
acos(x)	返回x的反余弦弧度值。

python数学常量
pi 数学常量pi(圆周率，一般以n来表示)
e 数学常量e，即自然常数