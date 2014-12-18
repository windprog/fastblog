#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-11
Desc    :   静态类，只实例化一次的类等
"""


class ErrorCode(object):
    """
        definitions for various Error Code.
        错误码部分来自微信错误码：http://mp.weixin.qq.com/wiki/17/fa4e1434e57290788bde25603fa2fcbd.html
    """

    SUCCESS = 0
    FAILED = -1

    ACCEPT = 200
    CREATE = 201
    BADREQUEST = 400
    UNAUTHORIZED = 401
    NOTFOUND = 404
    ERROR = 500

    # 开发者错误码定义
    WrongAccessToken = 40001  # 错误的access token
    ParameterMiss = 40002  # 参数缺失
    ParameterError = 40035  # 不合法的参数
    TargetNotFound = 40004  # 目标不存在

    ERROR_MESSAGE = {
        SUCCESS: u"Success",
        FAILED: u"Failed",

        ERROR: u"服务器内部错误",

        WrongAccessToken: u"错误的access token",
        ParameterMiss: u"参数缺失",
        ParameterError: u"不合法的参数",
        TargetNotFound: u"目标不存在",
    }