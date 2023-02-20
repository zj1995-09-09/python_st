# encoding: utf-8
# @author: MrZhou
# @file: 20函数.py
# @time: 2023/2/17 10:23
# @desc:

# 函数是组织好的，可重复使用用来实现单一或相关联功能的代码段
# 能提高应用的模块性，和代码的重复利用率。已经知道了python的内建函数 print(),也可以自己创建函数，这就叫做用户自定义函数
#
#
# def关键词开头，后接函数标识符名称和圆括号()
# 任何传入参数和自变量必须放在圆括号，圆括号之间可以用于定义参数
# 函数的第一行语句可以选择性使用文档字符串用于存放函数的说明
# 函数内容以冒号起始，并且缩进
# return[表达式]结束函数，选择性返回一个值给调用方。不带表达式的return相当于返回None


# def functionname( parameters ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
#
#
# 函数调用
# 定义一个函数只给了函数一个名称，指定函数里包含的参数和代码块结构
# 这个函数的基本结构完成以后，可以通过另一个函数调用执行，也可以直接从python提示符执行
#
# def printme(str):
#     '打印任何传入的字符串'
#     print str
#     return
#
# 调用函数
# printme('我要调用用户自定义函数')
# printme("再次调用同一函数")
#
# 参数传递
# 在python中，类型属于对象，变量是没有类型的
# a=[1,2,3]
# a="Runoob"
# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。

# 可更改与(mutable)与不可更改对象
# 在python中，string,tuple,numbers是不更改的对象
#
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
#
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

# 传可变对象实例
# 关键字参数和函数调用关系紧密


# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return


# 调用printme函数
# printme(str="My string")
#
#
# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print("Name: ", name)
#     print("Age ", age)
#     return


# 调用printinfo函数
# printinfo(age=50, name="miki")
#
# 默认参数
# 不定长参数 ：可能需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
#
# 加了星号*的变量名会存放所有未命名的变量参数，不定长参数实例如下
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return


# 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)
#
#
# 匿名函数lambda来创建匿名函数
# lambda的主题是一个表达式，函数体比def简单的多
# lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda表达式中封装有限的逻辑进去
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率

# lambda [arg1 [,arg2,.....argn]]:expression

# sum = lambda arg1, arg2: arg1 + arg2
# print(sum(10, 20))
#
#
# return语句
# return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None.之前的例子都没有示范如何返回数值


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
# total = sum(10, 20)
# 变量作用域 一个程序的所有的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量在哪里赋值的
# 变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称
#
# 全局变量
# 局部变量
#
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
#
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)
