#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-4
Desc    :   
"""
from fastblog.utils.wrapper import env_api, req_res_api, api_url


@api_url('/info/meta.json', "GET")
@env_api
def blog_info():
    return {
        'blogname': "Windpro's Blog"
    }





# pages
#=======================================================================================================================
#Paging navigator
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from fastblog.models import Posts


class MyPaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
        self.range_num = range_num
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)

    def page(self, number):
        self.page_number = number
        return super(MyPaginator, self).page(number)

    def _get_page_range_ext(self):
        page_range = super(MyPaginator, self).page_range
        start = long(self.page_number) - 1 - self.range_num / 2
        end = long(self.page_number) + self.range_num / 2
        if (start <= 0):
            end = end - start
            start = 0
        ret = page_range[start:end]
        return ret

    page_range_ext = property(_get_page_range_ext)

@api_url('/posts/mini/num:<page_count>,page:<num_page>.json', "GET")
@env_api
def mini_pages(page_count, num_page):
    posts_list = Posts.objects.all().filter(post_status='publish', post_type='post').order_by('-post_date')
    paginator = MyPaginator(posts_list, num_page)


    try:
        p_n = paginator.page(page_count)
    except EmptyPage:
        x = []

    contents = render_contents(page, more=more)

    if more:
        contents = render_contents(p_n, more=more)  #列表显示预览控制200个字符 read more...
    if nator == None:
        nator = render_nator(p_n)
    context = {
        'page_contents': contents,
        'page_nator': nator,
    }

    posts = [{}]
    return {
        'posts': []
    }