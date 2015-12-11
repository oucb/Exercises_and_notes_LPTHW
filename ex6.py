# -*- coding: utf-8 -*-
"""
Created on Wed Jun 04 11:10:22 2014

@author: oucb
"""
#!C:\Python27\python
# Filename:ex6.py

# let the string "There are 10 types of people." to x
x = "There are %d types of  people." % 10

binary = "binary"
do_not = "don't"

# let the string "Those who know binary and those who don't." to y
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print the string "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# combine the string of 'w' and 'e'
print w + e