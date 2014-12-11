#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-11
Desc    :   
"""
import datetime
import calendar
import json

# from bson.tz_util model
#=======================================================================================================================
from datetime import (timedelta,
                      tzinfo)

ZERO = timedelta(0)


class FixedOffset(tzinfo):
    """Fixed offset timezone, in minutes east from UTC.

    Implementation based from the Python `standard library documentation
    <http://docs.python.org/library/datetime.html#tzinfo-objects>`_.
    Defining __getinitargs__ enables pickling / copying.
    """

    def __init__(self, offset, name):
        if isinstance(offset, timedelta):
            self.__offset = offset
        else:
            self.__offset = timedelta(minutes=offset)
        self.__name = name

    def __getinitargs__(self):
        return self.__offset, self.__name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return ZERO


utc = FixedOffset(0, "UTC")
"""Fixed offset timezone representing UTC."""
#=======================================================================================================================


# from bson.__init__ model
#=======================================================================================================================
EPOCH_AWARE = datetime.datetime.fromtimestamp(0, utc)
#=======================================================================================================================



# 修改自 bson.json_util model
#=======================================================================================================================
def default(obj):
    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(calendar.timegm(obj.timetuple()) * 1000 +
                     obj.microsecond / 1000)
        return {"$date": millis}
    raise TypeError("%r is not JSON serializable" % obj)


def object_hook(dct):
    if "$date" in dct:
        secs = float(dct["$date"]) / 1000.0
        return EPOCH_AWARE + datetime.timedelta(seconds=secs)
    return dct
#=======================================================================================================================

NORMAL_TYPES = [
    int,
    datetime.datetime,
    unicode,
    str,
    bool,
]


def dumps(obj):
    return json.dumps(obj=obj, default=default)


def loads(aJsonString):
    return json.loads(aJsonString, object_hook=object_hook)


def get_jsonable_vars(obj):
    # 获取对象中基本类型的对象字典
    result = {}
    for name, value in vars(obj).iteritems():
        if type(value) in NORMAL_TYPES:
            result[name] = value
    return result