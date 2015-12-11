# -*- coding: utf-8 -*-
"""
Created on Wed May 28 09:56:38 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex21-3.py

l = print_string('name')
# 调用函数必须是在函数定义好后
print "length: %d" % l

def print_string(strs):
    print strs
    return len(strs)

