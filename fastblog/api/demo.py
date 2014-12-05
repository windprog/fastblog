#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-2
Desc    :   
"""
from httpappengine import url


@url("/test")
def hello(environ, start_response):
    s = "Hello, World!\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(s)))
    ])

    return s