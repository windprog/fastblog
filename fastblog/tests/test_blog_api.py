#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-12
Desc    :   
"""
from base import MockApiTestCase, TAG_URLS
from blog.api.blog import search

SEARCH_URI = getattr(search, TAG_URLS).keys()[0]


class BlogSearchTest(MockApiTestCase):
    def test_search_success(self):
        data = self.call_api_request(SEARCH_URI, "GET", params={
            'keyword': 'a',
            'page_count': "20",
            'num_page': "1",
            'mark_word': 'no'
        })
        self.assertKeysIncludeDict([
            "update_time",
            "title",
            "summary",
        ], data['posts'][0])