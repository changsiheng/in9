#!/usr/bin/env python
#coding:utf-8
'''
Created on Mar 30, 2016

@author: root
'''

def try_int(arg,default):
    ret = None
    try:
        arg = int(arg)
    except Exception,e:
        arg = default
    return arg
