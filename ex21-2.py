# -*- coding: utf-8 -*-
"""
Created on Wed May 28 09:29:56 2014

@author: oucb
"""

#!C:\Python27\python
# Filename:ex21-2.py

def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTUPLYING %d * %d" % (a,b)
    return a * b
    
def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a / b
    
print "Let's do some math with just fuctions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

m = divide(iq, 5)
n = multiply (weight, m)
y = subtract (height, n)
what = add(age, y)

print "That becomes:", what, "Can you do it by hand?"