#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 loretoparisi@gmail.com
#

from functools import wraps
from .bounded_pool_executor import BoundedThreadPoolExecutor
from .bounded_pool_executor import BoundedProcessPoolExecutor

_DEFAULT_POOL = BoundedThreadPoolExecutor(max_workers=5)
_PROCESS_POOL = BoundedProcessPoolExecutor(max_workers=5)

def threadpool(f, executor=None):
    @wraps(f)
    def wrap(*args, **kwargs):
        return (executor or _DEFAULT_POOL).submit(f, *args, **kwargs)

    return wrap

def processpool(f, executor=None):
    @wraps(f)
    def wrap(*args, **kwargs):
        return (executor or _PROCESS_POOL).submit(f, *args, **kwargs)

    return wrap
