#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-15
Desc    :   
"""
# test
from mongoengine import connect
connect(db='test', host='127.0.0.1', port=17117
        # , username='root', password='42bopwindpro'
)
from mongoengine import Document, StringField
class MPost(Document):
    title = StringField(max_length=120, required=True)

p = MPost()
p.title = 'test'
p.save()

for obj in MPost.objects:
    print obj.title, obj.id