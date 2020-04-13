#!/usr/local/bin/python3.7

import sys

def reverse_slicing(s):
  return s[::-1]

def reverse_case(s):
  mystr = ''
  for i in s:
    if i.isupper():
      mystr += i.lower()
    elif i.islower():
      mystr += i.upper()
    else:
      mystr += i
  return mystr

if len(sys.argv) <= 1:
  sys.exit()
sys.argv.pop(0)
mystr = ' '.join(sys.argv)
print(reverse_slicing(reverse_case(mystr)))

