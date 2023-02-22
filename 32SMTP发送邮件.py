# encoding: utf-8
# @author: MrZhou
# @file: 32SMTP发送邮件.py
# @time: 2023/2/22 10:06
# @desc:

SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
import smtplib
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
host：SMTP服务器主机可以指定主机的ip地址或者域名如：runoob.com
port：默认SMTP服务使用端口号为25
local_hostname:如果SMTP在你的本机，只需要指定服务器地址为localhost即可

smtpObj.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息
这里要注意一下第三个参数，msg 是字符串，表示邮件。
我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意 msg 的格式。
这个格式就是 smtp 协议中定义的格式

import smtplib
from email.mime.text import MIMEText
from email.header import Header