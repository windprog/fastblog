#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-10
Desc    :   路径相关方法
"""
from httpappengine import url
import config
'''
    API_BASE_PATH, DOMAIN 两个配置需要在系统后台动态调整
'''
# TODO:发送信号量，让子进程重新从数据库载入配置


def api_uri(path, methods="GET"):
    return url(config.API_BASE_PATH+path, methods)


def abs_url(uri):
    # 绝对路径
    assert not config.DOMAIN.endswith("/")
    return config.DOMAIN + uri
