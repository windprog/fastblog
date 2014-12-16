#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-12
Desc    :   
"""
import urllib
import json
import requests


def _call_http_request(url, method, body=None, params=None):
    if body is not None:
        body = json.dumps(body)

    param = ''
    if params is not None:
        param = '%s%s' % ('?' if '?' not in url else '', urllib.urlencode(params))

    r = getattr(requests, method.lower())('%s%s' % (url, param), data=body)

    return r


if __name__ == '__main__':
    print _call_http_request('https://api.github.com/search/users?q=<keyword>'.replace('<keyword>', 'testabcdefg'), "GET").text
    print '------------------'
    print _call_http_request('https://api.github.com/search/users', "GET", params={'q': 'testabcdefg'}).text
    print '------------------'
    print _call_http_request('https://api.github.com/search/users?c=test', "GET", params={'q': 'testabcdefg'}).text
    print '------------------'
