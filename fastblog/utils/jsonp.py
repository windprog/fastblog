#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-4
Desc    :   
"""
import base64

def get_jsonp_callback_name(PATH_INFO):
    return base64.encodestring(PATH_INFO)