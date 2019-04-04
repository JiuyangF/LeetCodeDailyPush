# -*- coding: utf-8 -*-
# @Time    : 2019-03-29 4:00 PM
# @Author  : jiuyang
# @File    : __init__.py.py
import json
f = open('midas/s_txt','r')

s1 = json.loads(f.read())
print(s1)

