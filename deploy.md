# 使用ansible一键部署
---------------------------
写了一个ansible的脚本: `deploy-blog-simple.yml <deploy-blog-simple.yml>`_

在配置好ansible之后，可以一句话完成部署操作::

    $ ansible-play deploy-blog-simple.yml

这样执行完成之后，程序会在你配置好的服务器上自动的搭建虚拟环境，并安装依赖，启动blog程序，监听在8000端口，直接可以通过ip+端口进行访问: http://your-ip:8000 ，后台地址:http://your-ip:8000/xadmin 。

**用户名/密码** 均为 **the5fire**

不了解ansible的童鞋可以看下这里: `ansible中文指南 <http://www.the5fire.com/ansible-guide-cn.html>`_
