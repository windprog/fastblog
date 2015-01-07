#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14/12/21
Desc    :   
"""
import os
import sys
# 添加项目引用路径
PROJECT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)
# 载入用户配置
os.environ.setdefault("APPENGINE_SETTINGS_MODULE", "config")
from httpappengine.aetest import start_mock, BaseHttpTestCase
from httpappengine.util import get_action_uri


class ApiTestCase(BaseHttpTestCase):
    pass

start_mock()