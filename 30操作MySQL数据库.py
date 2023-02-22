# encoding: utf-8
# @author: MrZhou
# @file: 30操作MySQL数据库.py
# @time: 2023/2/21 20:01
# @desc:


Python 标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口。
# MySQLdb 是用于Python链接Mysql数据库的接口，它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。
#
# $ gunzip MySQL-python-1.2.2.tar.gz
# $ tar -xvf MySQL-python-1.2.2.tar
# $ cd MySQL-python-1.2.2
# $ python setup.py build
# $ python setup.py install

# 数据库连接 确认以下事项
#
# 您已经创建了数据库 TESTDB.
# 在TESTDB数据库中您已经创建了表 EMPLOYEE
# EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
# 连接数据库TESTDB使用的用户名为 "testuser" ，密码为 "test123"
# 你可以可以自己设定或者直接使用root用户名及其密码，Mysql数据库用户授权请使用Grant命令。
# 在你的机子上已经安装了 Python MySQLdb 模块。
#
# pip install PyMySQL
# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
# # __author__ = "shuke"
# # Date: 2018/5/13

import pymysql

# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user='zff', passwd='zff123', db='zff', charset='utf8mb4')

# 创建游标(查询数据返回为元组格式)
# cursor = conn.cursor()

# 创建游标(查询数据返回为字典格式)
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 1. 执行SQL,返回受影响的行数
effect_row1 = cursor.execute("select * from USER")

# 2. 执行SQL,返回受影响的行数,一次插入多行数据
effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)", [("jack"), ("boom"), ("lucy")])  # 3

# 查询所有数据,返回数据为元组格式
result = cursor.fetchall()

# 增/删/改均需要进行commit提交,进行保存
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

print(result)
"""
[{'id': 6, 'name': 'boom'}, {'id': 5, 'name': 'jack'}, {'id': 7, 'name': 'lucy'}, {'id': 4, 'name': 'tome'}, {'id': 3, 'name': 'zff'}, 
{'id': 1, 'name': 'zhaofengfeng'}, {'id': 2, 'name': 'zhaofengfeng02'}]
"""

# 执行事务 事务机制可以确保数据一致性
# 事务应该具有4个属性：原子性、一致性、隔离性、持久性 ACID
# 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
# 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
# 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
# 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。

对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。

commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。