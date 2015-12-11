# -*- coding: utf-8 -*-
"""
Created on Thu May 15 09:45:17 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex14-1.py

from sys import argv

script,user_name,favorite = argv
prompt = 'Please input:'

print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What kind of thing do you like best? %s?" % favorite 
favorites = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r coumputer. Nice.
Also, you like playing %r. Me too.
""" % (likes,lives,computer,favorite)
