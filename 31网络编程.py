# encoding: utf-8
# @author: MrZhou
# @file: 31网络编程.py
# @time: 2023/2/21 20:22
# @desc:

python提供了两个级别访问的网络服务
低级别的网络服务支持基本的Socket 提供了标准的BSD socket API，可以访问底层操作系统Socket接口的全部方法
高级别的网络服务模块SocketServer,它提供了服务器中心类，可以简化网络服务器的开发

Socket又称套接字，应用程序通常通过套接字向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯

socket()函数来创建套接字，语法格式
socket.socket([family[, type[, proto]]])

服务端
使用socket模块的socket函数来创建一个socket对象。socket对象可以通过调用其他函数来设置一个socket服务
可以调用bind(hostname,port)函数来指定服务的port
接着，调用socket对象的accept方法，等待客户端的连接并返回connection对象，表示已连接到客户端

# import socket #导入socket模块
# s=socket.socket #创建socket对象
# host=socket.gethostname() #获取本地主机名
# port=12345 #设置端口
# s.bind((host, port)) #绑定端口
#
# s.listen(5)  #等待客户端连接
# while True:
#     c,addr=s.accept() #建立客户端连接
#     print('连接地址：'addr)
#     c.send('欢迎访问菜鸟教程！')
#     c.close() #关闭连接

客户端
简单的客户端连接到以上创建的服务，端口号为12345
socket.connect(hostname,port)方法打开一个TCP连接到主机为hostname端口为port的服务商
连接后我们就可以从服务端获取数据，记住操作完成后需要关闭连接


# import socket # 导入 socket 模块
# s=socket.socket() # 创建 socket 对象
# host=socket.gethostname() # 获取本地主机名
# port =12345 # 设置端口号
#
# s.connect((host, port))
# print(s.recv(1024))
# s.close()

# 现在我们打开两个终端，第一个终端执行 server.py 文件：
#
# $ python server.py
# 第二个终端执行 client.py 文件：
#
# $ python client.py
# 欢迎访问菜鸟教程！
# 这时我们再打开第一个终端，就会看到有以下信息输出：
#
# 连接地址： ('192.168.0.118', 62461)

协议	功能用处	端口号	Python 模块
HTTP	网页访问	80	httplib, urllib, xmlrpclib
NNTP	阅读和张贴新闻文章，俗称为"帖子"	119	nntplib
FTP	文件传输	20	ftplib, urllib
SMTP	发送邮件	25	smtplib
POP3	接收邮件	110	poplib
IMAP4	获取邮件	143	imaplib
Telnet	命令行	23	telnetlib
Gopher	信息查找	70	gopherlib, urllib
