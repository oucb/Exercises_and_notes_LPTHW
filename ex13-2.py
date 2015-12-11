# -*- coding: utf-8 -*-
"""
Created on Fri May 09 09:15:34 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex13-2.py

from sys import argv

script,time,day,month,year = argv

print "The script is called:",script
print "The current time is:",time
print "Today is '%s.%s.%s'" % (day,month,year)

