# -*- coding: utf-8 -*-
"""
Created on Fri May 09 14:15:12 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex13-3.py

from sys import argv

script,name =argv

print "The script is called",script
print "%s,how old are you?" % name,
age = raw_input()
print "%s,how tall are you?" % name,
height = raw_input()
print "%s,how much do you weigh?" % name,
weight =raw_input()

print "So,%s,you are %r old,%r tall and %r heavy." % (name,age,height,weight)
