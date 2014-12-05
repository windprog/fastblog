#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-4
Desc    :   
"""


class Router(object):
    class InstanceDescriptor(object):
        def __get__(self, *args, **kwargs):
            owner = kwargs.get("kwargs")
            v = getattr(owner, "__instance__", None)
            if not v:
                v = owner()  # 构造参数!
                owner.__instance__ = v
            return v

    def __init__(self):
        self.test = "a"
        print 'init'

    handlers = property(lambda self: self._handlers)
    instance = InstanceDescriptor()

def func(obj):
    pass

func(Router.instance.test)