#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-4
Desc    :   
"""
from .http import s_r_api, r_api
import urlparse
from .jsonp import get_jsonp_callback_name
from httpappengine.decorator import parse_wrapper_return
from httpappengine import url


def get_api_kwargs(environ):
    path_info = environ.get("PATH_INFO")
    query_string = environ.get("QUERY_STRING")
    query_dict = urlparse.parse_qs(query_string)
    api_kwargs = {}
    if "callback" in query_dict:
        #使用uri生成函数名
        api_kwargs['json'] = get_jsonp_callback_name(path_info)
    return api_kwargs

@parse_wrapper_return
def env_api(handler):
    # 使用这个wrapper更节省资源
    # 不生成request和response
    def env_handler(environ, start_response, **kwargs):
        handler_args = handler.func_code.co_varnames[:handler.func_code.co_argcount]
        assert "response" not in handler_args and "request" not in handler_args
        if "environ" in handler_args:
            kwargs['environ'] = environ
        if "start_response" in handler_args:
            kwargs['start_response'] = start_response

        data = handler(**kwargs)

        api_kwargs = get_api_kwargs(environ)

        return s_r_api(start_response=start_response, header={}, data=data, **api_kwargs)

    return env_handler

@parse_wrapper_return
def req_res_api(handler):
    # 生成request, response
    def req_res_handler(request, response, environ, start_response, **kwargs):
        handler_args = handler.func_code.co_varnames[:handler.func_code.co_argcount]
        assert "start_response" not in handler_args
        if "request" in handler_args:
            kwargs["request"] = request
        if "response" in handler_args:
            kwargs["response"] = response
        if "environ" in handler_args:
            kwargs["environ"] = environ

        data = handler(**kwargs)

        api_kwargs = get_api_kwargs(environ)

        return r_api(response=response, header={}, data=data, **api_kwargs)

    return req_res_handler


API_BASE_PATH = '/blogcache'


def api_url(path, methods="GET"):
    return url(API_BASE_PATH+path, methods)