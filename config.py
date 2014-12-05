#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-2
Desc    :   
"""
# 详细配置说明请参考appengine/engine/config.py
DEBUG = True

# 服务器监听地址。
HOST = "0.0.0.0"
PORT = 8888

# 需要载入的Action 模块
ACTIONS = [
    "fastblog.api",
    "plugs"
]

SUPPORT_DJANGO = True
DJANGO_SETTINGS_MODULE = "django_setting.settings"
DJANGO_URLS = [
    # "/demo"
]