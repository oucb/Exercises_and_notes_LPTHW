# -*- coding: utf-8 -*-
"""
Created on Thu May 08 09:52:03 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex10-1.py

print "What is your name?",
name = raw_input()
print "How old are you?",
age = raw_input()
print "What do you like?",
love = raw_input()

print "I can call you %r,you are %r old and you like %r." % (name,age,love)