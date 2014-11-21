#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-11-18
Desc    :   rss生成
"""

from django.contrib.syndication.views import Feed
from fastblog.models import Posts, Comments
from fastblog.templatetags.myfilter import autop_filter


class CommentsFeed(Feed):
    title = u"evilbinary博客评论"
    link = u"/blog/feeds/rss2"
    description = u"关注evilbinary博客"

    def items(self):
        return Comments.objects.select_related('comment_post').filter(comment_post__post_status='publish',
                                                                      comment_post__post_type='post').order_by(
            'comment_date')[:50]

    def item_title(self, item):
        return item.comment_post.post_title

    def item_description(self, item):
        return autop_filter(item.comment_content)

    def item_link(self, item):
        return "/blog/article/" + str(item.comment_id)

    def author_name(self, obj):
        return 'evilbinary'

    def author_email(self, obj):
        return 'windprog@gmail.com'


class ArticlesFeed(Feed):
    title = u"evilbinary博客"
    link = "/blog/feeds/rss2"
    description = u"关注evilbinary博客"
    author_email = "windprog@gmail.com"
    author_name = "evilbinary"

    def items(self):
        return Posts.objects.filter(post_status='publish', post_type='post').order_by('-post_date')[:50]

    def item_title(self, item):
        return item.post_title

    def item_description(self, item):
        return autop_filter(item.post_content)

    def item_link(self, item):
        return "/blog/article/" + str(item.id)

    def author_name(self, obj):
        return 'evilbinary'

    def author_email(self, obj):
        return 'windprog@gmail.com'


