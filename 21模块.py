# encoding: utf-8
# @author: MrZhou
# @file: 21模块.py
# @time: 2023/2/17 15:34
# @desc:

# python模块module，是一个python文件，以.py结尾包含了python对象定义和python语句
# 模块让你能够让你有逻辑的组织你的python代码段
# 把相关的代码分配到一个模块里能够让你的代码更好用，更易懂
# 模块能定义函数，类和变量，模块也能包含可执行的代码


def print_func(par):
    print("Hello : ", par)
    return


# import 语句
# 模块的引入
# import模块名、函数名
# 当解释器遇到import,如果模块在当前的搜索路径就会被导入
# 搜索路径是一个解释器会先进行搜索的所有目录的列表，如果想要导入模块support.py,需要把命令放在脚本的顶端
# 一个模块只会被导入一次，不管你执行了多少次import ,这样可以防止导入模块被一遍又一遍的执行
#
#
# from *** import (*)
# 从模块中导入一个指定的部分到当前命名空间中
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的
# from modname import *
#
# 搜索路径
# 当你导入一个模块，python解释器对模块位置的搜索顺序是
# 1、当前目录
# 2、如果不在当前目录，python则搜索在shell变量PYTHONPATH下的每个目录
# 3、如果都找不到，python会查看默认路径。UNIX下，默认路径一般为/usr/local/lib/python
#
# 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录

# PYTHONPATH 变量 作为环境变量，由装在一个列表里的许多目录组成，PYTHON的语法和shell变量PATH的一样
# Windows系统，
# set PYTHONPATH =c:\python27\lib;
# 在UNIX系统，典型的PYTHONPATH如下：
# set PYTHONPATH=/usr/local/lib/python
#
#
# Python 会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
#
# 因此，如果要给函数内的全局变量赋值，必须使用 global 语句
# global varName的表达式会告诉python VarName 是一个全局变量，
Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)

我们在全局命名空间定义一个变量Money,我们再在函数内给变量Money赋值，然后python会假定Money是一个局部变量。
然而，我们并没有访问前声明一个局部变量Money，结果就是会出现一个UnboundLocalError的错误
取消global语句前的注释就能解决这个问题


dir函数
返回的列表容纳了在一个模块里定义的所有模块，变量和函数
import math
content =dir(math)
print(content)
__name__是指向模块的名字，__file__是指向该模块的导入文件名

globals()和local()函数
根据调用地方的不同，globals()和local()函数可被用来返回全局和局部命名空间里的名字
如果在函数内部调用locals(),返回的是所有能在该函数里访问的命名
如果在函数内部调用globals(),返回的是所有在该函数里能访问的额全局名字
两个函数的返回类型都是字典，所以名字们能用keys()函数摘取

reload()函数
当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次
因此如果想重新执行模块里顶层部分的代码，可以用reload()函数，该函数会重新导入之前导入过的模块
reload(module_name) module_name 直接放模块的名字，而不是一个字符串形式

python包
定义了一个由模块及子包，和子包下的子包等组成的python的应用环境 就是一个文件夹
但该文件夹必须存在__init__.py文件
test.py
package_runoob
__init__.py
__runoob1.py
__runoob2.py

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('package_runoob初始化')

然后再package_runoob同级目录下创建test.py来调用package__runoob的包
举例为D:\测试\python_st\test

在每个文件里放置了一个函数，但其实可以放置许多函数，也可以在这些文件里定义python的类然后为这些类建一个包


