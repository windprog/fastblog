#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-12
Desc    :   
"""
from base import ApiTestCase
from blog.api.blog import search, index, recently_posts, hots_posts, category_posts, tags_posts, detail_posts, \
    category_available


class BlogSearchTest(ApiTestCase):
    Func = search

    def test_search_success(self):
        data = self.call_api_request(self.get_api_uri(), method="GET", params={
            'keyword': 'a',
            'page_count': "20",
            'num_page': "1",
            'mark_word': 'no'
        })
        self.assertTrue("post" in data)
        self.assertKeysIncludeDict(
            [
                "update_time",
                "title",
                "summary",
            ], data['post'][0])


class IndexTest(ApiTestCase):
    Func = index

    def test_index_success(self):

        data = self.call_api_request(self.get_api_uri().replace("<int:page_index>", "1"))
        self.assertTrue("post" in data)
        self.assertTrue(len(data["post"]) > 0)
        self.assertKeysIncludeDict(["title", "alias"], data["post"][0])


class RecentlyPostsTest(ApiTestCase):
    Func = recently_posts

    def test_recently_posts(self):
        data = self.call_api_request(self.get_api_uri())
        self.assertTrue("post" in data)


class HotPostTest(ApiTestCase):
    Func = hots_posts

    def test_hots_posts_success(self):
        data = self.call_api_request(self.get_api_uri())
        self.assertTrue("post" in data)
        self.assertTrue(len(data["post"]) > 0)
        self.assertKeysIncludeDict(["title", "alias"], data["post"][0])

class CatePostsTest(ApiTestCase):
    Func = category_posts

    def test_category_posts_success(self):
        data = self.call_api_request(self.get_api_uri().replace("id:<int:category_id>,page:<int:page_index>", "id:1,page:1"))
        self.assertTrue("post" in data)
        self.assertTrue(len(data["post"]) > 0)
        self.assertKeysIncludeDict(["title", "alias"], data["post"][0])