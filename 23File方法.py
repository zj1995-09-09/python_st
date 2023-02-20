# encoding: utf-8
# @author: MrZhou
# @file: 23File方法.py
# @time: 2023/2/20 14:06
# @desc:

open()方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数
如果该文件无法被打开，会抛出OSError
常用形式是接收两个参数，文件名(file) 和模式(mode)
open(file=,mode='r')


file对象使用open函数来创建
# file 对象的属性
# 一个文件被打开后，你有一个file对象
# file.closed 返回TRUE如果文件已被关闭，否则返回false
# file.mode 返回被打开文件的访问模式
# file.name 返回文件的名称

file.next()
返回文件下一行

file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力

file.tell()
返回文件当前位置


file.truncate([size])
截取文件，截取的字节通过size指定，默认为当前文件位置

file.write(str)
将字符串写入文件，返回的是写入的字符长度