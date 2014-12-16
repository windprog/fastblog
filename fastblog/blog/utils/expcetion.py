#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-11
Desc    :   
"""
from static import ErrorCode


class ApiException(Exception):
    '''全局错误码exception，搭配ErrorCode使用'''
    def __get_message(self, error_code):
        return ErrorCode.ERROR_MESSAGE.get(error_code, u"未识别错误码")

    def __init__(self, error_code):
        self.error_code = error_code
        self.message = self.__get_message(self.error_code)