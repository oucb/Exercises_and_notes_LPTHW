# -*- coding: utf-8 -*-
"""
Created on Wed May 21 08:32:04 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex18.py

# this one is like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# ok, that *args is actually pointless, we can just do this 
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# this one takes no arguments
def print_none():
    print "I got nothin'."
    
print_two("Zed","shaw")
print_two_again("Zed","shaw")
print_one("First!")
print_none()