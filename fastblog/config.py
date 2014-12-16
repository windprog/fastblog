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
PORT = 8001

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
    DOMAIN = 'http://localhost:8000'
else:
    DOMAIN = 'http://www.codedig.com'

# 这一项需要在系统设置中更改
API_BASE_PATH = '/blogcache/api'