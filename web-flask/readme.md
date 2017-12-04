### python-flask 学习
1.) 基础需求
* python 基础
* 前端 (html/css)
* 数据库表设计
  + 一对一、一对多、多对多、外键

2.) 工具
* Pycharm2016
* sublime
* MySQL

3.) 学习目标
* 熟悉 Flask 相关知识
* 属性 web 开发流程
* 能独立开发 Flask 项目


安装环境
* windows 安装 Python 2.7 （官网下载）
  + 添加环境变量 ptyhon
  + 添加 pip 环境变量

python 虚拟环境介绍与安装
  + 版本不兼容问题
  + cmd -> pip install virtualenv
  + 开辟新的虚拟环境 virtualenv [virtualenv-name]
  + 激活虚拟环境
    + 直接进入到 虚拟环境目录执行 activate
  + 退出虚拟环境
    + deactivate

pip 安装 Flask
  + pip install flask

### 认识 web
1.) url 统一资源定位符
  + 协议 http/https
  + 主机 host
  + 端口 port 80/443
  + 路径 path
  + 查询字符串 query-string (key = value)
  + 锚点 anchor 前端定位页面用
2.) web 服务器和应用服务器以及web应用框架
  + web 服务器
    + 负责处理 http 请求，响应静态文件，常见的有 Apache，Nginx 以及微软的 IIS
  + 应用服务器
    + 负责逻辑处理的服务器，如 php、python 的代码 不能通过 nginx 这种   web 服务器来处理，常见的应用服务器有 uwsgi、tomcat 等
  + web 应用框架
    + 一般使用某种语言，封装了常用的 web 功能的框架就是 web 应用框架，flask、Django 以及 JAVA 中的 SSH 框架都是 web 应用框架
