# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     aioip __init__.py
   Description :
   Author :       LateautunmLin
   date：          2018/9/8
-------------------------------------------------
   Change Activity:
                   2018/9/8:
-------------------------------------------------
"""
__author__ = 'LateautunmLin'

from pathlib import Path
current = Path(__file__)
for i in current.iterdir():
    print(i)
