#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-10
Desc    :   
"""
from ..utils.wrapper import env_api, req_res_api
from ..utils.path import api_uri
from ..utils.ujson import get_jsonable_vars
import config


def pages(query_args, query_kwargs, page_count=20, num_page=1, obj_callback=None):
    from ..models import Post
    from django.core.paginator import Paginator
    all_posts = Post.objects.defer('content', 'content_html')\
        .filter(*query_args, **query_kwargs)
    # 翻页
    paginator = Paginator(all_posts, page_count)
    posts = paginator.page(num_page)
    result = []
    for post in posts:
        if obj_callback:
            # 回调函数
            obj_callback(post)
        result.append(get_jsonable_vars(post))
    return result


class ObjVarReplace(object):
    # 替换对象内 字符串字段
    def __init__(self, word, field, format_str):
        # 被替换的值
        self._word = word
        # 被替换的字段
        if isinstance(field, str):
            self._field_names = [field]
        elif isinstance(field, list):
            self._field_names = field
        else:
            raise TypeError()
        # 替换格式，如'x{0}x'
        self._format_str = format_str

    def __call__(self, obj):
        for name in self._field_names:
            setattr(obj, name, getattr(obj, name).replace(self._word, self._format_str.format(self._word)))


class PostReplace(ObjVarReplace):
    def __init__(self, word):
        super(PostReplace, self).__init__(
            word, field=['title', 'summary'], format_str='<span class="hightline">{0}</span>')


# no cache
#=======================================================================================================================

@api_uri('/posts/search.json', "GET")
@env_api
def search(keyword, page_count=20, num_page=1, mark_word=False):
    from django.db.models import Q
    query_kwargs = dict(status=0)
    query_args = ()
    pp = None
    if keyword:
        query_args = (
            (
                Q(title__icontains=keyword) |
                Q(content__icontains=keyword)
            ),
        )
        if mark_word:
            pp = PostReplace(word=keyword)

    result = pages(
        query_args=query_args, query_kwargs=query_kwargs, page_count=page_count,
        num_page=num_page, obj_callback=pp
    )
    return {
        'posts': result
    }

#=======================================================================================================================

# pages
@api_uri('/posts/index/page:<int:num_page>.json', "GET")
@env_api
def index(num_page=1):
    return {
        'posts': pages(
            query_args=(), query_kwargs={}, page_count=config.PAGE_COUNT, num_page=num_page
        )
    }


#=======================================================================================================================

@api_uri('/info/meta.json', "GET")
@env_api
def blog_info():
    return {
        'blogname': "Windpro's Blog"
    }

@api_uri('/posts/mini/num:<int:page_count>,page:<int:num_page>.json', "GET")
@env_api
def mini_pages(page_count, num_page):

    posts = [{}]
    return {
        'posts': []
    }