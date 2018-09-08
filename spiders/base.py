# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     aioip base
   Description :
   Author :       LateautunmLin
   date：          2018/9/8
-------------------------------------------------
   Change Activity:
                   2018/9/8:
-------------------------------------------------
"""
__author__ = 'LateautunmLin'

class BaseSpider(type):
    def __new__(cls,name,bases,attrs):
        return super(BaseSpider, cls).__new__(cls, name, bases, attrs)
