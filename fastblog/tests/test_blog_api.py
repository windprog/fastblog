#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-12
Desc    :   
"""
from base import ApiTestCase, get_action_uri
from blog.api.blog import search, index, recently_posts, hots_posts, category_posts, tags_posts, detail_posts, \
    category_available


class BlogSearchTest(ApiTestCase):
    def test_search_success(self):
        data = self.call_json_request(get_action_uri(search), method="GET", params={
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
    def test_index_success(self):
        data = self.call_json_request(get_action_uri(index).replace("<int:page_index>", "1"))
        self.assertTrue("post" in data)
        self.assertTrue(len(data["post"]) > 0)
        self.assertKeysIncludeDict(["title", "alias"], data["post"][0])


class RecentlyPostsTest(ApiTestCase):
    def test_recently_posts(self):
        data = self.call_json_request(get_action_uri(recently_posts))
        self.assertTrue("post" in data)


class HotPostTest(ApiTestCase):
    def test_hots_posts_success(self):
        data = self.call_json_request(get_action_uri(hots_posts))
        self.assertTrue("post" in data)
        self.assertTrue(len(data["post"]) > 0)
        self.assertKeysIncludeDict(["title", "alias"], data["post"][0])


class CatePostsTest(ApiTestCase):
    def test_category_posts_success(self):
        data = self.call_json_request(
            get_action_uri(category_posts).replace("id:<int:category_id>,page:<int:page_index>", "id:1,page:1"))
        self.assertTrue("post" in data)
        self.assertTrue(len(data["post"]) > 0)
        self.assertKeysIncludeDict(["title", "alias"], data["post"][0])


class TagsPostsTest(ApiTestCase):
    def test_tags_posts_success(self):
        data = self.call_json_request(
            get_action_uri(tags_posts).replace("name:<tag_name>,page:<int:page_index>", "name:标,page:1"))
        self.assertTrue("post" in data)
        self.assertTrue(len(data["post"]) > 0)
        self.assertKeysIncludeDict(["title", "alias"], data["post"][0])


class DetailPostsTest(ApiTestCase):
    def test_detail_posts_success(self):
        data = self.call_json_request(get_action_uri(detail_posts).replace("<int:post_id>", "1"))
        self.assertKeysIncludeDict(["title", "alias", "next_post", "prev_post"], data)


class CateAvailableTest(ApiTestCase):
    def test_category_available_success(self):
        data = self.call_json_request(get_action_uri(category_available))
        self.assertTrue("category" in data)
        self.assertTrue(len(data["category"]) > 0)
        self.assertKeysIncludeDict(["name", "alias"], data["category"][0])


if __name__ == '__main__':
    import unittest
    unittest.main()