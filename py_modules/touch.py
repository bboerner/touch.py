#!/usr/bin/env python
import os
from os.path import dirname, exists
# me
from fullpath import fullpath
from public import public

@public
def touch(path):
    # todo: add datetime
    if not path: return
    path = fullpath(path)
    if path.find("/")>0 and not exists(dirname(path)):
        os.makedirs(dirname(path))
    try:
        os.utime(path,None)
    except:
        open(path,'a').close()
