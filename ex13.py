#!/usr/bin/env python

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("What's your fourth variable? ")
fifth = raw_input("What's your fifth variable? ")
print "Your fourth and fifth variables are %r and %r." % (fourth, fifth)
