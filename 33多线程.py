# encoding: utf-8
# @author: MrZhou
# @file: 33多线程.py
# @time: 2023/2/22 10:20
# @desc:

# 多线程类似同时执行多个不同程序
# 使用线程可以把占据长时间的程序中的任务放到后台处理
# 用户界面可以更加吸引人，用户点击了一个按钮出发某些事件的处理，可以弹出一个进度条来显示处理的进度
# 程序的运行速度可能加快
# 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程比较有用 可以释放一些珍贵的资源如内存占用等
#
# 线程在执行过程中与进程还是有区别的。每个独立的进程有一个程序运行的入口、顺序执行序列和程序的出口。
# 但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。

# 每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态
# 指令指针和堆栈指针寄存器是线上上下文中两个最重要的寄存器，线程总是在进程中得到上下文中运行的
# 这些地址都用于标志拥有线程的进程地址空间中的内存
#
# 线程可以被抢占中断
# 在其他线程正在运行时，线程可以暂时搁置(也称为睡眠)--这就是线程的退让

# python中使用线程有两种方式：函数或者类来包装线程对象
#
# 函数式：调用thread模块中的start_new_thread()函数产生新线程
#
# thread.start_new_thread( function, args[, kwargs] )
# function-线程函数
# args-传递给线程函数的参数，必须是tuple类型
# kwargs-可选参数

import threading
import time

# 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
#
# # 创建两个线程
# try:
#     threading.start_new_thread(print_time, ("Thread-1", 2,))
#     threading.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print("Error: unable to start thread")
#
# while 1:
#     pass


# 线程模块
# 通过两个标准库thread和threading提供对线程的支持，thread提供了低级别的、原始的线程以及一个简单的锁
#
# threading模块提供的其他方法
# threading.current_thread():返回当前的线程变量
# threading.enumerate():返回一个包含正在运行的线程的list,正在运行指线程启动后，结束前，不包括启动前和终止后的线程
# threading.activeCount():返回正在运行的线程数量，与len(threading.enumerate())有相同的结果
#
# 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

# import threading
# import time
#
# exitFlag = 0
#
#
# class myThread(threading.Thread):  # 继承父类threading.Thread
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
#         print
#         "Starting " + self.name
#         print_time(self.name, self.counter, 5)
#         print
#         "Exiting " + self.name
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             (threading.Thread).exit()
#         time.sleep(delay)
#         print
#         "%s: %s" % (threadName, time.ctime(time.time()))
#         counter -= 1
#
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启线程
# thread1.start()
# thread2.start()
#
# print
# "Exiting Main Thread"

# 线程同步
# 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
# 使用Thread对象的lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法 对于那些需要每次只允许一个线程
# 操作的数据，可以将其操作放到acquire和release方法之间
#
# 考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
#
# 那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
# 锁有两种状态-锁定和未锁定。每当一个线程比如set要访问共享数据时，必须要获得锁定，如果已经有别的线程比如print获得
# 锁定，那么就让线程set暂停，也就是同步阻塞，等到线程print访问完毕，释放锁以后再让线程set继续
#
# 经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。

import threading
import time

exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print("Exiting Main Thread")


线程优先级队列(queue)
提供了同步的、线程安全的队列类，包括FIFO 先入先出队列queue，LIFO后入先出队列LifoQueue
和优先级队列priorityQueue,这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步

queue模块中的常用方法:


# Queue.qsize() 返回队列的大小
# Queue.empty() 如果队列为空，返回True,反之False
# Queue.full() 如果队列满了，返回True,反之False
# Queue.full 与 maxsize 大小对应
# Queue.get([block[, timeout]])获取队列，timeout等待时间
# Queue.get_nowait() 相当Queue.get(False)
# Queue.put(item, block=True, timeout=None) 写入队列，timeout等待时间
# Queue.put_nowait(item) 相当 Queue.put(item, False)
# Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
# Queue.join() 实际上意味着等到队列为空，再执行别的操作
