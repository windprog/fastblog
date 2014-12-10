#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-9
Desc    :   
"""
DEBUG = True

# 服务器监听地址。
HOST = "0.0.0.0"
PORT = 8000

# 需要载入的Action 模块
ACTIONS = [
    "blog.api",
]

SUPPORT_DJANGO = True
DJANGO_SETTINGS_MODULE = "blog.django_setting.settings"
DJANGO_URLS = [
    # "/demo"
]