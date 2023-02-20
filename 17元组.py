# encoding: utf-8
# @author: MrZhou
# @file: 17元组.py
# @time: 2023/2/16 11:36
# @desc:
# python 元祖与列表类似，不同之处在于元祖的元素不能被修改
# tup1=()
# 元组中只包含一个元素时 需要在元素的后面添加逗号
# tup1=(50,)
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等
# 修改元组是不允许的，但我们可以对元组进行连接组合
tup1 = (12, 34, 56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的
# tup1[0]=100
#
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组
# 元组中的元素是不允许删除的，但我们可以用del语句删除整个元组
# del tup3
# print(tup3)

# 元组运算符 可以使用+ *进行运算
# 元组索引，截取
# 无关闭分隔符，任意无符号的对象，以逗号隔开，默认为元组

print('abc', -4.24e93, 18 + 6.6j, 'xyz')
x, y = 1, 2
print("Value of x , y : ", x, y)

# 元组内置函数
# cmp(tup1, tup2) 比较两个元组元素
# len(tup1, tup2)
# max(tup1)
# min(tup1)
# tuple(seq) 将列表转换为元组
