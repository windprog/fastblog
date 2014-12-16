#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-10
Desc    :   
"""
import urlparse
import sys
from httpappengine.decorator import parse_wrapper_return

from .http import s_r_api, r_api
from .func import get_jsonp_callback_name
from .expcetion import ApiException
from .static import ErrorCode

MAX_INT_NUM = len(str(sys.maxint))


def __get_query_dict(environ):
    # 处理get参数字典
    # 将只有一个元素的字典变为该元素
    query_string = environ.get("QUERY_STRING")
    query_dict = urlparse.parse_qs(query_string)
    result = {}
    for name, value in query_dict.iteritems():
        result[name] = value[0] if len(value) == 1 else value
    return result


def __get_api_kwargs(path_info, query_dict):
    # get参数字典如果存在callback，则按照jsonp进行处理
    api_kwargs = {}
    if "callback" in query_dict:
        #使用uri生成函数名
        api_kwargs['jsonp'] = get_jsonp_callback_name(path_info)
    return api_kwargs


def __assert_handler_default_type(index, value, handler_args, handler_defaults):
    # handler 保证默认参数与实际参数 类型相同
    if handler_defaults:
        # 函数默认参数的下标
        default_index = index - (len(handler_args) - len(handler_defaults))
        if default_index >= 0:
            if not type(handler_defaults[default_index]) == type(value):
                # 当默认参数和实际传入参数不符时引发 api参数错误
                raise ApiException(ErrorCode.ParameterError)


def __parse_handler_kwargs(des_dict, handler_args, handler_defaults, handler_kwargs):
    # 业务函数参数处理
    for name, value in des_dict.iteritems():
        try:
            index = handler_args.index(name)
        except ValueError, e:
            # 传入的参数不在 目标函数参数列表（如**kwargs）
            continue
        if index >= 0:
            # 将yes no 替换成布尔
            if value == "yes":
                value = True
            elif value == "no":
                value = False
            elif len(value) <= MAX_INT_NUM:
                # 必须作为最后的判断手段
                # 尝试转换int
                try:
                    value = int(value)
                except Exception, e:
                    pass
            __assert_handler_default_type(index, value, handler_args, handler_defaults)
            handler_kwargs[name] = value


def __parse_wrapper(environ, handler, handler_args, kwargs):
    # 各类api wrapper的集中处理函数
    if "environ" in handler_args:
        #统一加入environ
        kwargs['environ'] = environ
    path_info = environ.get("PATH_INFO")
    query_dict = __get_query_dict(environ)

    # handler 默认参数 值列表
    handler_defaults = handler.func_defaults

    # 处理jsonp调用情况
    api_kwargs = __get_api_kwargs(path_info, query_dict)
    method = environ.get('REQUEST_METHOD').upper()
    if method == "GET":
        # 将http get参数传递给函数
        # 处理默认参数类型，保证默认参数与实际传入参数类型一致
        try:
            __parse_handler_kwargs(query_dict, handler_args, handler_defaults, kwargs)
        except ApiException, e:
            data = {
                "error_code": e.error_code,
                "message": e.message
            }
            return data, api_kwargs, kwargs

    # 处理业务函数 内部错误 和 缺少参数
    try:
        data = handler(**kwargs)
    except TypeError, e:
        if e.message.startswith(handler.__name__ + "("):
            # 业务函数缺少参数，一般为get参数缺少必要参数
            e = ApiException(ErrorCode.ParameterMiss)
            data = {
                "error_code": e.error_code,
                "message": e.message
            }
        else:
            raise e
    except ApiException, e:
        data = {
            "error_code": e.error_code,
            "message": e.message
        }

    return data, api_kwargs, kwargs

@parse_wrapper_return
def env_api(handler):
    # 使用这个wrapper更节省资源
    # 不生成request和response
    def env_handler(environ, start_response, **kwargs):
        handler_args = handler.func_code.co_varnames[:handler.func_code.co_argcount]
        assert "response" not in handler_args and "request" not in handler_args
        if "start_response" in handler_args:
            kwargs['start_response'] = start_response

        data, kwargs, api_kwargs = __parse_wrapper(environ, handler, handler_args, kwargs)

        return s_r_api(start_response=start_response, header={}, data=data, **api_kwargs)

    return env_handler


@parse_wrapper_return
def req_res_api(handler):
    # 这个需要生成request, response，比较耗资源
    def req_res_handler(request, response, environ, start_response, **kwargs):
        handler_args = handler.func_code.co_varnames[:handler.func_code.co_argcount]
        assert "start_response" not in handler_args
        if "request" in handler_args:
            kwargs["request"] = request
        if "response" in handler_args:
            kwargs["response"] = response

        data, kwargs, api_kwargs = __parse_wrapper(environ, handler, handler_args, kwargs)

        return r_api(response=response, header={}, data=data, **api_kwargs)

    return req_res_handler