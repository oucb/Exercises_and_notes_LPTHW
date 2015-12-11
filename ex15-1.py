# -*- coding: utf-8 -*-
"""
Created on Fri May 16 10:09:50 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex15-1.py

from sys import argv

script = argv

print "Type the filename:"
filename = raw_input('>')

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input('>')

txt_again = open(file_again)

print txt_again.read()