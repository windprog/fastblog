#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-9
Desc    :   项目配置文件，其他配置请参考httpappengine.engine.config.settings
"""
DEBUG = True

# 服务器监听地址。
HOST = "0.0.0.0"
PORT = 8000

# 需要载入的Action 模块
ACTIONS = [
    "blog.api",
    "plugs"
]

SUPPORT_DJANGO = True
DJANGO_SETTINGS_MODULE = "blog.django_setting.settings"
DJANGO_URLS = [
    # "/demo"
]

if DEBUG:
    DOMAIN = 'http://localhost:%s' % PORT
else:
    DOMAIN = 'http://www.codedig.com'

# 这一项需要在系统设置中更改
API_BASE_PATH = '/blogcache/api'

# 博客设置
PAGE_NUM = 20
RECENTLY_NUM = 15
HOT_NUM = 15
ONE_DAY = 24*60*60
FIF_MIN = 15 * 60
FIVE_MIN = 5 * 60
