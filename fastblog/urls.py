#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-11-18
Desc    :   url定义
"""

from django.conf.urls import *
from fastblog import views
from django.conf import settings
from fastblog.views import *
from django.contrib import admin
from feeds import ArticlesFeed, CommentsFeed

urlpatterns = patterns(
    'fastblog.views',
    url(r'^$', 'index'),
    url(r'^archive/(\d{4})/(\d{1,2})/$', 'archive'),
    url(r'^article/(\d+)/$', 'article'),
    url(r'^articles/(\d{4})/$', 'year_archive'),
    url(r'^articles/(\d{4})/(\d{2})/$', 'month_archive'),
    url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'article_detail'),
    url(r'^pages(?P<num>\d+)/$', 'pages'),
    url(r'^pages/$', 'pages'),
    url(r'^pages/(?P<num>\d+)/$', 'pages'),
    url(r'^page/(?P<page_id>\d+)$', 'page'),
    url(r'^test(?P<num>\d+)/$', 'page'),
    url(r'^comment', 'comment'),
    url(r'^search/$', 'search'),
    url(r'^cat/(?P<num>\d+)$', 'cat'),
    url(r'^archives/(?P<num>\d+)/$', 'archives'),
    url(r'^archives$', 'archives'),
    url(r'^feeds/rss2$', ArticlesFeed()),
    url(r'^feeds/comments-rss2$', CommentsFeed()),
    url(r'^feeds/(?P<str>\S+)$', 'feed'),
    url(r'^test$', 'test'),
    url(r'^page_expir$', 'page_expir'),
)