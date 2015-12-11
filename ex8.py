# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 14:36:29 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex8.py

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didin't sing,",
    "So I said goodnight."
    )