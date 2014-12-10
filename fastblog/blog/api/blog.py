#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-10
Desc    :   
"""
from ..utils.wrapper import env_api, req_res_api, api_url


@api_url('/info/meta.json', "GET")
@env_api
def blog_info():
    return {
        'blogname': "Windpro's Blog"
    }





# pages
#=======================================================================================================================

@api_url('/posts/mini/num:<page_count>,page:<num_page>.json', "GET")
@env_api
def mini_pages(page_count, num_page):

    posts = [{}]
    return {
        'posts': []
    }