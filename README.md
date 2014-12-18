#fastblog
=========
博客地址: http://codedig.com

##描述

    Fastblog 是一个专注于为网络差的服务器编写的python博客，可将博客放置于国外服务器获得类似国内服务器的效果。
    本博客系统基于Django1.7.1开发而成，通过[appengine](https://github.com/windprog/appengine)运行。
    具有插件机制，可将插件放置于plugs目录即可载入。

##功能特点
* 使用[appengine](https://github.com/windprog/appengine)构建api和插件体系，拒绝任何依赖保证主系统代码量少。
* 静态文件、模板和文章内容都放置在各种cdn中保证快速访问（目前支持百度云、之后支持七牛云储存）
* 发布文章和评论实时显示（需要模板支持，可看默认模板的实现）,具体刷新类型请看订阅类型文档。
* 后台管理采用django框架
* 以文件夹分割的插件体系，可随时删除单独插件不影响其他部分（例如你不需要七牛云储存，只需要删除fastblog/plugs/qiniudn/，django后台会同时删除菜单）。
* 支持markdown，SyntaxHighlighter语法高亮功能。
* 支持多种数据库(sqlite、mysql等)。
* 文章、分类和页面的增删改查
* 通过rst格式或者html格式书写文章正文
* 侧边栏的组件化调整（目前比较弱）
* 集成多说的评论
* RSS和rpc
* 微信后台


##接下来实现
* 动态发布静态资源，将地址存入数据库，可在后台选择删除，想法来自[前端工程](https://app.yinxiang.com/shard/s33/sh/f2eeff73-d852-47f8-b9d7-79a4abf5d16e/41f47bfacf5a8853a0eab7a5ad61f43a)


##目录结构

    |--conf                 -- 项目相关工具配置文件
    |--fastblog             -- 项目根目录
       |--api               -- 项目前端api相关接口
       |--plugs             -- 插件目录
       |--templates         -- 博客模板
       |--blog              -- django设置
          |--django_setting	-- django设置
          |--...            -- 建模和相关后台模板
       |--utils             -- 常用方法包
       |--manage.py         -- django管理
       |--run.py            -- 运行项目


##将要废弃的目录地址(转移代码结构)

    |--fastblog
       |--blog
          |--templates      -- 博客模板


##在线演示
* [http://codedig.com](http://codedig.com) (这里是个人[博客地址](http://codedig.com)，也就是用本开源软件搭建的。)
* [https://github.com/windprog/fastblog](https://github.com/windprog/fastblog) （源码地址 ）

##安装说明
首先下载源码，可以直接点击[download](https://github.com/windprog/fastblog/archive/master.zip)，也可以在shell下输入:
	
	git clone https://github.com/windprog/fastblog.git

安装pip：

    sudo apt-get install python-pip -y

httpappengine依赖gevent，先安装gevent依赖库：libevent

    sudo apt-get install python-dev gcc libevent-dev -y

安装virtualenv

    sudo pip install virtualenv

创建虚拟环境

    virtualenv env

保证硬盘有足够空间，cd到目录env中，执行

    cd env
    # 激活虚拟环境
    source bin/activate
    # 安装依赖包
    pip install -r ../requirements.txt

进入项目目录

    cd ../fastblog

创建数据库或表

    # 针对sqlite3,mysql的话需要先创建数据库然后修改settings中的配置
    # 在django_selfblog/selfblog目录下执行
    python manage.py syncdb


运行

    # 直接运行
    python manage.py runserver

    #或者
    python run.py

访问

    http://localhost:8000


#Done List
* 规划项目目标（后台django、前端全分布式静态、post部分动态、数据实时更新）

#TODO
* 增加comment模型
* 重构fastblog，将所有数据变为http api，写好avalon前端数据实时刷新js库，方便随时变换前端。
* 参考[newBlog](https://github.com/BeginMan/newBlog)
* 参考[zhihu-python](https://github.com/egrcc/zhihu-python)api模板编写方式
* * 编写wiki模块
* * 七牛云储存模块
* * [命令行发送博客文件](https://github.com/BeginMan/pytool/blob/master/spider/autoSendSaeBlog.py)
* 参考[uliweb](https://github.com/limodou/uliweb)编写readme.md文档
* 添加博客文章：[tornado源码分析](https://app.yinxiang.com/view/notebook/075b8b77-cc87-417e-90db-a949b3be7b98?locale=zh_CN_ENCHINA#b=fba9a22d-0214-411f-982e-67bbe7ccb4a8&st=p&n=075b8b77-cc87-417e-90db-a949b3be7b98)
* 添加博客文章：iptables学习笔记（参考以前的[icmp_tunnel](https://github.com/windprog/icmp-tunnel)）
* 添加文章：ipdb使用学习笔记[pdb](http://www.cnblogs.com/dkblog/archive/2010/12/07/1980682.html)
* 支持微信公共平台
* 继承django db，重写save方法，远程保存到mongodb
* 完成之后requirements.txt里锁定所有依赖库版本

#插件架构
* 采用内存数据库redis
* 每一个子进程都保存一份当前修改尚未同步的api列表（地址，时间戳）（广播方案:redis、[pipe](http://f.dataguru.cn/thread-44651-1-1.html)）
* * 客户端为此都带上一次访问(页面刷新或者上一次订阅api)时间戳的请求订阅api，返回该时间戳到现在所有去重订阅类型数据api地址。（js.DOMAIN有主域和缓存域列表，在每一次请求页面的时候返回）
* * 在不同的页面类型访问有不同的订阅地址，订阅类型：
* * * 文章详细-文章（<全文章api>）
* * * 文章详细-评论（评论首页api，用first_id请求<id文章评论已更新列表api>）
* * * 分类列表-首页文章
* * * 分类列表-最新文章
* * * 分类列表-系列文章（实际上是新增隐藏分类）
* * * 分类列表-全站热门
* * * 分类列表-最新评论
* * * 首页-...(跟分类列表一样)
* * 同步完成的api会向所有子进程广播完成信息，其他子进程删除列表对象