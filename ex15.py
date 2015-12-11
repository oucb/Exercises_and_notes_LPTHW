# -*- coding: utf-8 -*-
"""
Created on Thu May 15 14:31:10 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex15.py

#import argument variable from sys module
from sys import argv

#unpack argv to two variables:script and filename 
script,filename = argv

#pass the value of the file 'filename' to argument txt
txt = open(filename)

#print the contents of txt through the fuction 'read'
print "Here's your file %r:" % filename
print txt.read()

#print and prompt user to input the name of a file
print "Type the filename again:"
file_again = raw_input(">")

#pass the content of the file 'file_again' to argument txt_again
txt_again = open(file_again)

#print the contents of the file txt_again 
print txt_again.read()
