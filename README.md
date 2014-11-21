#Fastblog
=========
Fastblog 是一个专注于为网络差的服务器编写的python博客，可将博客放置于国外服务器获得类似国内服务器的效果。

你可以随时下载使用，部分代码参考[myblog](https://github.com/evilbinary/myblog)
#特点
* 使用[appengine](https://github.com/windprog/appengine)构建api和插件体系，拒绝任何依赖保证主系统代码量少。
* 静态文件、模板和文章内容都放置在各种cdn中保证快速访问（目前支持百度云、之后支持七牛云储存）
* 发布文章和评论实时显示（需要模板支持，可看默认模板的实现）
* 后台管理采用django框架
* 以文件夹分割的插件体系，可随时删除单独插件不影响其他部分（例如你不需要七牛云储存，只需要删除fastblog/plugs/qiniudn/，django后台会同步删除菜单）。
* 支持markdown，SyntaxHighlighter语法高亮功能。
* 支持多种数据库(sqlite、mysql等)。

#目录结构
> * fastblog			-- 项目文件夹
> * * templates			-- 后台管理模板
> * django_setting		-- django设置，一般不需要更改
> * templates			-- 前端模板文件夹

#在线演示
* [http://codedig.com](http://codedig.com) (这里是个人[博客地址](http://codedig.com)，也就是用本开源软件搭建的。)
* [https://github.com/evilbinary/myblog](https://github.com/evilbinary/myblog) （源码地址 ）

#截图
* 博客首页 ![前台博客](https://github.com/evilbinary/myblog/raw/master/data/screen-shot1.png)
* 博客后台管理  ![前台博客](https://github.com/evilbinary/myblog/raw/master/data/screen-shot2.png)

#安装说明
===================
##linux
在苹果系统下安装很容易，首先下载源码，可以直接点击download下载，[猛击这里，注意安全！](https://github.com/evilbinary/myblog/archive/master.zip)，也可以在shell下输入:
	
	git clone https://github.com/windprog/fastblog.git
	
下载好后，如果是压缩包记得解压，进去后可以看到setup.py这个就是安装文件了，注意你需要有python环境,运行:
	
	python setup.py
	
然后让它自己安装，安装好后，到项目路径里面，可以看到fastblog、manage.py、templates等，然后运行：

	python manage.py syncdb

同步一下数据库，可能叫你输入第一次创建超级用户，你就输入一个用户，还有密码，成功后应该有个db.sqlite文件出来，再次运行：
	
	python manage.py runserver
	
如果没看到错误，那就可以启动服务器了，让后打开浏览器输入:[http://localhost:8088/](http://localhost:8088/)就可以看到界面了。

#Done List
* 规划项目目标（后台django、前端全分布式静态、post部分动态、数据实时更新）

#TODO
* 重构fastblog，将所有数据变为restfull api，写好avalon同步js库，方便随时变换前端。
* 参考[newBlog](https://github.com/BeginMan/newBlog)
* * 编写wiki模块
* * 七牛云储存模块
* * [命令行发送博客文件](https://github.com/BeginMan/pytool/blob/master/spider/autoSendSaeBlog.py)
* 添加博客文章：[tornado源码分析](https://app.yinxiang.com/view/notebook/075b8b77-cc87-417e-90db-a949b3be7b98?locale=zh_CN_ENCHINA#b=fba9a22d-0214-411f-982e-67bbe7ccb4a8&st=p&n=075b8b77-cc87-417e-90db-a949b3be7b98)
* 添加博客文章：iptables学习笔记（参考以前的[icmp_tunnel](https://github.com/windprog/icmp-tunnel)）