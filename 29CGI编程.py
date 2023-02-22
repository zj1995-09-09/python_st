# encoding: utf-8
# @author: MrZhou
# @file: 29CGI编程.py
# @time: 2023/2/21 19:44
# @desc:

CGI目前由NCSA维护
common gateway interface 通用网关接口，是一段程序运行在服务器上，如HTTP服务器，提供同客户端HTML页面的接口

网页浏览
点击一个链接或者URL的流程：
1、使用你的浏览器访问URL并连接到HTTP web 服务器
2、Web 服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容 否则返回错误信息
3、浏览器从服务器上上接收信息，并显示接收的文件或者错误信息

CGI程序可以是python脚本，Perl脚本，shell脚本 C++程序


web服务器支持及配置
Apache 支持 CGI 配置：

设置好CGI目录：

ScriptAlias /cgi-bin/ /var/www/cgi-bin/
所有的HTTP服务器执行 CGI 程序都保存在一个预先配置的目录。这个目录被称为 CGI 目录，并按照惯例，它被命名为 /var/www/cgi-bin 目录
CGI 文件的扩展名为 .cgi，python 也可以使用 .py 扩展名。
默认情况下，Linux 服务器配置运行的 cgi-bin 目录中为 /var/www。

浏览器客户端通过两种方法向服务器传递信息，这两种方法就是GET方法和POST方法

