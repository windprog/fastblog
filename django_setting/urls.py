#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-11-18
Desc    :   配置
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('fastblog.urls')),
    url(r'^blog/', include('fastblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)