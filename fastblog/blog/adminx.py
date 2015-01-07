#coding:utf-8
import xadmin
from django.core import urlresolvers
from django.db.models import F

from .models import Post
from .models import Category
from .models import Page
from .models import Widget
from .models import Tag
from .utils.markup import restructuredtext


class PostAdmin(object):
    search_fields = ('title', 'alias')
    fields = ('title', 'content', 'summary', 'alias', 'tags', 'pub_time', 'status',
              'category', 'is_top')
    list_display = ('preview', 'title', 'category', 'is_top', 'pub_time')
    list_display_links = ('title', )

    ordering = ('-pub_time', )
    list_per_page = 15
    save_on_top = True

    def preview(self, obj):
        url_edit = urlresolvers.reverse('xadmin:blog_post_change', args=(obj.id,))
        return u'''
                    <span><a href="/%s.html" target="_blank">预览</a></span>
                    <span><a href="%s" target="_blank">编辑</a></span>
                ''' % (obj.alias, url_edit)

    preview.short_description = u'操作'
    preview.allow_tags = True

    # todo need test
    def parse_tag(self):
        obj = self.new_obj
        old_post = Post.objects.get(id=obj.id)

        cut_tag_list = []
        if old_post:
            new_tags = set(obj.tags_list())
            old_tags = set(old_post.tags_list())
            # 新增的tag
            new_tag_list = list(new_tags - old_tags)
            # 需要删除的tag
            cut_tag_list = list((new_tags | old_tags) - new_tags)
        else:
            new_tag_list = obj.tags_list()

        for tag in new_tag_list:
            try:
                old_tag = Tag.objects.get(name=tag)
                old_tag.update(post_count=F('post_count') + 1)
            except Tag.DoesNotExist:
                ot = Tag(name=tag, post_count=1)
                ot.save()
        for tag in cut_tag_list:
            # 减少的tag
            Tag.objects.get(name=tag).update(post_count=F('post_count') - 1)

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        if not obj.summary:
            obj.summary = obj.content
        obj.content_html = restructuredtext(obj.content)

        self.parse_tag()

        obj.save()


class CategoryAdmin(object):
    search_fields = ('name', 'alias')
    list_display = ('name', 'rank', 'is_nav', 'status', 'create_time')


class PageAdmin(object):
    search_fields = ('name', 'alias')
    fields = ('title', 'alias', 'link', 'content', 'is_html', 'status', 'rank')
    list_display = ('title', 'link', 'rank', 'status', 'is_html')

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        if obj.is_html:
            obj.content_html = obj.content
        else:
            obj.content_html = restructuredtext(obj.content)
        obj.save()


class WidgetAdmin(object):
    search_fields = ('name', 'alias')
    fields = ('title', 'content', 'rank', 'hide')
    list_display = ('title', 'rank', 'hide')


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Page, PageAdmin)
xadmin.site.register(Widget, WidgetAdmin)
