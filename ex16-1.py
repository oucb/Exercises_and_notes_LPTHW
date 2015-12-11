# -*- coding: utf-8 -*-
"""
Created on Tue May 20 13:29:47 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex16-1.py

from sys import argv

script,filename = argv

print "The file is called %s." % filename

t = open(filename)

print t.read()
