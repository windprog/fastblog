#MyBlog
=========
"myblog"是清凉干净的一个开源django的博客,你可以随时下载使用。
#特点
* 兼容wordpress博客系统,数据从wordpress迁移过来毫无压力。
* 支持markdown，SyntaxHighlighter语法高亮功能。
* 支持多种数据库(sqlite、mysql等)。
	
	
# 在线演示
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
	
然后让它自己安装，安装好后，到wsgi文件夹里面，有个叫mysite这个就是项目的路径，可以看到blog、manage.py、templates等，然后运行：

	python manage.py syncdb

同步一下数据库，可能叫你输入第一次创建超级用户，你就输入一个用户，还有密码，成功后应该有个db.sqlite文件出来，再次运行：
	
	python manage.py runserver
	
如果没看到错误，那就可以启动服务器了，让后打开浏览器输入:[http://localhost:8088/](http://localhost:8088/)就可以看到界面了。