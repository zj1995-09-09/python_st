# encoding: utf-8
# @author: MrZhou
# @file: 27面向对象.py
# @time: 2023/2/21 13:47
# @desc:

# 类Class:用来描述具有相同的属性和方法的对象的集合，定义了该集合中每个对象所共有的属性和方法
# 对象是类的实例
class Employee:
    empCount = 0

    def __int__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d " % Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, "salary:", self.salary)


# empCount变量是一个类变量，它的值将在这个类的所有实例之间共享
# 可以在内部类或外部类使用Employee.empCount
# 第一种方法__init__()是一种特殊的方法，被称为类的构造函数或初始化方法
# 当创建了这个类的实例时就会调用该方法
#
# self代表类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数

# 实例化:创建一个类的实例，类的具体对象
# 实例化类其他编程语言中一般用关键字new，但是在python中并没有 类似函数调用方式
# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)
#
# 访问属性 使用点号访问对象的属性 使用类的名称访问类变量
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount
#
#
# python内置类属性
# __dict__:类的属性 包含一个字典，由类的数据属性组成
# __doc__:类的文档字符串
# __name__:类名
# __module__:类定义所在的模块(类的全名是"__main__.className",如果类位于一个导入模块mymod中，那么className.__module__等于mymod)
# __bases__:类的所有父类构成元素(包含了一个由所有父类组成的元组)
#
# python对象销毁(垃圾回收)
# 使用了引用计数这一简单技术来跟踪和回收垃圾
# 在python内部记录着所有使用中的对象各有多少引用
# 一个内部跟踪变量，称为一个引用计数器
# 当对象被创建时，就创建了一个引用计数，当对象不再需要时，也就是说这个对象的引用计数变为0时，它被垃圾回收
# 但是回收不是立即的，由解释器在适当的时机将垃圾对象占用的内存空间回收

# 实例变量：在类的声明中属性是变量来表示的。这种变量称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的

# 类变量：在整个实例化的对象中是公用的，类变量定义在类中且在函数体之外
# 类变量通常不作为实例变量使用
#
# 数据成员：类变量或者实例变量，用于处理类及其实例对象的相关的数据
#
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写
# 过程叫做方法的覆盖override，也称为方法的重写
#
# 局部变量：定义在方法中的变量，只作用于当前实例的类
#

#
# 继承：一个派生类derived class继承基类 base class 的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
# 面向对象的编程带来的好处之一是代码的重用，实现这种重用的方法之一是通过继承机制
# 通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类


class Parent:
    parentAttr=100
    def  __int__(self):
        print('调用父类构造函数')
    def parentMethod(self):
        print('调用父类方法')
    def setAttr(self,attr):
        Parent.parentAttr=attr
    def getAttr(self):
        print('父类属性:',Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print('调用子类方法')
    def childMethod(self):
        print('调用子类方法')

c=Child()
c.childMethod()
c.parentMethod()调用父类方法
c.setAttr()
c.getAttr()

# 方法重写
#
# 基础重载方法
# __init__
# __del__
#
# 类的私有属性
# __private_attrs:两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问
# 在类的内部的方法中使用时self.__private_attrs
#
# 类的方法
# 在类的内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
#
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods
#
# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
# class Runoob:
#     __site = "www.runoob.com"
#
# runoob = Runoob()
# print runoob._Runoob__site


单下划线、双下划线、头尾双下划綫

__foo__:定义的是特殊方法，一般是系统定义名字，类似__init__()之类
_foo:表示的是protected类型变量，即保护类型只能允许其本身与子类进行访问，不能用于from module import *
__foo:双下划线表示私有类型private变量 只能允许这个类本身进行访问了

#
# 一个Dog类型的对象派生自Animal类，这是模拟
# "是一个（is-a）"dog是一个Animal）。
#

#
# 方法:类中定义的函数
#
# 对象:通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法
