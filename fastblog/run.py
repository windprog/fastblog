#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-9
Desc    :   
"""
import os
from httpappengine.util import run_server

os.environ.setdefault("APPENGINE_SETTINGS_MODULE", "config")

run_server()