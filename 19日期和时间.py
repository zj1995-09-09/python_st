# encoding: utf-8
# @author: MrZhou
# @file: 19日期和时间.py
# @time: 2023/2/16 15:26
# @desc:

# python程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能
# python提供了一个time和calendar模块可以用于格式化日期和时间
# 时间间隔是以秒为单位的浮点小数
#
# 每个时间戳都以自1970年1月1日午夜(历元)经过了多长时间来表示
# python time 模块下有很多函数可以转换常见日期格式，如time.time()用于获取当前时间戳

import time

# ticks = time.time()
# print("当前时间戳为：", ticks)
# 时间戳单位最适合做日期运算 ，但是1970年之前的日期就无法以此表示了，太遥远的日期也不行，UNIX和Windows只支持到2038年
#
#
# 获取格式化时间，可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()
localtime = time.asctime(time.localtime((time.time())))
# print("本地时间为：", localtime)
#
#
# 格式化日期
# 可以用time模块的strftime方法来格式化日期：
print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

# python中时间日期格式化符号：
#
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00-59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# 获取某月日历 calendar模块
import calendar

cal = calendar.month(2023, 3)
print("以下输出20023年3月份的日历")
print(cal)

# time内置函数，既有事件处理和转换时间格式
# time.asctime([tupletime])
# 接受时间元组并返回一个可读的形式

# calendar.month(year, month, w=2, l=1)
# 返回一个多行字符串格式的year年month月日历，两行标题，一周一行，每日宽度间隔为w字符。每行的长度为7*w+6.l是每星期的行数

cal2 = calendar.weekday(year=2023, month=2, day=5)
print(cal2)
返回6 给定日期的日期码礼拜六
