# encoding: utf-8
# @author: MrZhou
# @file: 24异常处理.py
# @time: 2023/2/20 14:20
# @desc:
import os


# python提供了两个非常功能处理python程序在运行中出现的异常和错误
# 异常处理：
# 断言Assertions
#
# 异常即是一个事件，该事件会在程序执行过程中发生影响了程序的正常执行
# 一般情况下python无法正常处理程序时就会发生一个异常
# 异常是python对象，表示一个错误
# 当python脚本发生异常时我们需要捕获处理它，否则程序会终止执行
#
# 异常处理
# 捕捉异常可以使用try/except语句
# try语句块中的错误，从而让except语句捕获异常信息并处理
# 如果你不想在异常发生时结束你的程序，只需在try里捕获它
# 工作原理是 开始一个try语句后，python就在当前程序的上下文忠作出标记，这样当异常出现时就可以回到这里，
# try子句先执行，接下来会发生什么依赖于执行时是否出现异常


# os.chmod()
# try:
#     fh = open("testfile", "w")
#     fh.write('这是一个测试文件，用于测试异常！')
# except IOError:
#     print('Error:没有找到文件或读取文件失败')
# else:
#     print('内容写入文件成功')
#     fh.close()
#
#
# 使用except而不带任何异常类型
# 可以不带任何异常类型使用expect，如下实例
# 不是一个很好的方式不能通过该程序识别出具体的异常信息，因为它捕获所有的异常
#
# try:
#     正常的操作
# except:
#     发生异常，执行这块代码
# else:
#     如果没有异常执行这块代码
#
# 使用expect而带多种异常类型
# try:
#     正常的操作
# except(Exception1[,Exception2]):
#     发生以上多个异常中的一个，执行这块代码
# else:
#     如果没有异常执行这行代码
#
# try-finally 语句无论发生异常都将执行最后的代码
# try:
#     语句
# finally:
#     语句 退出try时总会执行
# raise

# try:
#     fh1 = open('testfile', 'w')
#     fh1.write('第二次这是一个测试文件，用于测试异常！')
# finally:
#     print('Error:没有找到文件或读取文件失败')


# try:
#     fh1 = open('testfile', 'w')
#     try:
#         fh1.write("第三次这是一个测试文件，用于测试异常")
#     finally:
#         print('关闭文件')
#         fh1.close()
# except IOError:
#     print("Error:没有找到文件或读取文件失败")
#
#
# 异常的参数
# 一个异常可以带上参数，可作为输出的异常信息参数可以通过except语句来捕获异常的参数
# try:
#     正常的参数
# except ExceptionType,Argument:
#     你可以在这输出Argument的值
#
# 变量接收的异常值通常包含在异常的语句中，在元组的表单中变量可以接收一个或多个值
# 元组通常包含错误字符串，错误数字，错误位置

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("参数没有包含数字\n", Argument)


# 调用函数
temp_convert("xyz")
#
# 触发异常可以使用raise语句自己触发异常
# raise[Exception[,args[,traceback]]]
# 语句中Exception 是异常的类型，例如NameError参数标准异常中任一种，args是自己提供的异常参数
# 最后一个参数是可选的

# 一个异常可以是一个字符串，类或对象。python的内核提供的异常，大多数都是实例化的的类，这是一个类的实例的参数

def mye(level):
    if level < 1:
        raise Exception("Invalid level!")
        # 触发异常后，后面的代码就不会再执行


try:
    mye(0)  # 触发异常
except Exception as err:
    print(1, err)
else:
    print(2)


用户自定义异常
创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类
在try语句块中，用户自定义的异常后执行except,