#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-10
Desc    :   response相关设置函数
"""
import json


JSON_CONTENT_TYPE = "application/json; charset=utf-8"
CORS = "*.codedig.com"
format_str = "{func_name}({json_str});"
default_header = {
    "Cache-Control": "no-cache",
    "Content-Type": JSON_CONTENT_TYPE,
    'Access-Control-Allow-Origin': CORS
}


def parse_result(result, api_kwargs):
    if "jsonp" in api_kwargs:
        result = format_str.format(
            func_name=api_kwargs.get("jsonp"),
            json_str=result
        )
    return result


def s_r_api(start_response, header, data, **kwargs):
    # 使用start_response来返回json数据
    # 存在jsonp则为jsonp返回方式，值为jsonp callback方法名
    s = json.dumps(data)
    s = parse_result(s, kwargs)

    r_header = {
        "Content-Length": str(len(s))
    }
    r_header.update(default_header)
    default_header.update(header)

    start_response("200 OK", [(k, v) for k, v in default_header.iteritems()])

    return (s,)


def from_response_set_default_header(response):
    """ response content-type is 'application/json'.
    """
    from httpappengine.engine.config import settings
    # response
    if not isinstance(response, settings.Response):
        raise TypeError("response must be Response instance")

    response.headers.update(default_header)


def r_api(response, header, data, **kwargs):
    # 使用response来设置json数据
    # 存在jsonp则为jsonp返回方式，值为jsonp callback方法名
    from_response_set_default_header(response)
    response.status_code = 200
    response.set_data(parse_result(json.dumps(data), kwargs))
    for k, v in header.iteritems():
        response.headers.setdefault(k, v)
