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
from ..models import Post, Category


def pages(all_posts, page_num=20, page_index=1, obj_callback=None):
    from django.core.paginator import Paginator
    result = []
    # 翻页
    paginator = Paginator(all_posts, page_num)
    posts = paginator.page(page_index)
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

@api_uri('/post/search.json', "GET")
@env_api
def search(keyword, page_num=20, page_index=1, mark_word=False):
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
        all_posts=Post.objects.defer('content', 'content_html').filter(*query_args, status=0),
        page_num=page_num, page_index=page_index, obj_callback=pp
    )
    return {
        'post': result
    }

#=======================================================================================================================

# post
# 首页
@api_uri('/post/index/page:<int:page_index>.json', "GET")
@env_api
def index(page_index=1):
    return {
        'post': pages(
            all_posts=Post.objects.defer('content', 'content_html').filter(status=0),
            page_num=config.PAGE_NUM, page_index=page_index
        )
    }

# 最近发表的文章
@api_uri('/post/recently.json', "GET")
@env_api
def recently_posts():
    return {
        'post': [get_jsonable_vars(post) for post in Post.get_recently_posts(config.RECENTLY_NUM)]
    }

# 热门文章
@api_uri('/post/hots.json', "GET")
@env_api
def hots_posts():
    return {
        'post': [get_jsonable_vars(post) for post in Post.get_hots_posts(config.HOT_NUM)]
    }

# 分类文章
@api_uri('/post/category/id:<int:category_id>,page:<int:page_index>.json', "GET")
@env_api
def category_posts(category_id, page_index):
    category = Category.objects.get(id=category_id)
    if category:
        result = pages(
            all_posts=category.post_set.defer('content', 'content_html').filter(status=0),
            page_num=config.PAGE_NUM, page_index=page_index
        )
    else:
        result = []
    return {
        'post': result
    }

# 标签文章
@api_uri('/post/tag/name:<tag_name>,page:<int:page_index>.json', "GET")
@env_api
def tags_posts(tag_name, page_index):
    return {
        'post': pages(
            all_posts=Post.objects.defer('content', 'content_html').filter(tags__icontains=tag_name, status=0),
            page_num=config.PAGE_NUM, page_index=page_index
        )
    }

# 文章详情
@api_uri('/post/detail/<int:post_id>.json', "GET")
@env_api
def detail_posts(post_id):
    from ..utils.cache import cache
    post = get_jsonable_vars(Post.objects.get(id=post_id))
    next_id, prev_id = post.id + 1, post.id - 1

    def get_post_info(_id):
        try:
            _post = Post.objects.get(id=_id)
            return dict(title=_post.title, id=_post.id, alias=_post.alias)
        except Post.DoesNotExist:
            return None

    post['next_post'] = get_post_info(next_id)
    post['prev_post'] = get_post_info(prev_id)

    post['other_views'] = cache.get('lru_views', {}).items()

    post['related_posts'] = post.related_posts

    return post

# category
# 页面展示的分类列表
@api_uri('/category/available.json', "GET")
@env_api
def category_available():
    return {
        'category': [get_jsonable_vars(category) for category in Category.available_list()]
    }




#=======================================================================================================================

@api_uri('/info/meta.json', "GET")
@env_api
def blog_info():
    return {
        'blogname': u"Windpro's Blog",
        'description': u"关于编程（python,js等）、设计模式、系统（linux）、开源–人生苦短，我用python",
        'keywords': u"python,linux,vim,web开发,工作经验,项目实战,教程",
        'author': u"Windpro"
    }

@api_uri('/posts/mini/num:<int:page_num>,page:<int:page_index>.json', "GET")
@env_api
def mini_pages(page_num, page_index):

    posts = [{}]
    return {
        'posts': []
    }