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


# no cache
#=======================================================================================================================

@api_uri('/posts/search.json', "GET")
@env_api
def search(keyword, page_count=20, num_page=1, mark_word=False):
    from django.db.models import Q
    from ..models import Post
    from django.core.paginator import Paginator

    if keyword:
        qset = (
            Q(title__icontains=keyword) |
            Q(content__icontains=keyword)
        )
        all_posts = Post.objects.defer('content', 'content_html')\
            .filter(qset, status=0)
    else:
        all_posts = Post.objects.defer('content', 'content_html')\
            .filter(status=0)
    paginator = Paginator(all_posts, page_count)
    posts = paginator.page(num_page)
    result = []
    for post in posts:
        if mark_word:
            post.title = post.title.replace(keyword, '<span class="hightline">%s</span>' % keyword)
            post.summary = post.summary.replace(keyword, '<span class="hightline">%s</span>' % keyword)
        result.append(get_jsonable_vars(post))
    return {
        'posts': result
    }

#=======================================================================================================================

# pages
#=======================================================================================================================

@api_uri('/info/meta.json', "GET")
@env_api
def blog_info():
    return {
        'blogname': "Windpro's Blog"
    }

@api_uri('/posts/mini/num:<page_count>,page:<num_page>.json', "GET")
@env_api
def mini_pages(page_count, num_page):

    posts = [{}]
    return {
        'posts': []
    }