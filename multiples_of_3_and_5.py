#!/usr/bin/env python2.7
"""
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.  

Author: Dan Granillo <dan.granillo@gmail.com>

"""

def getDivs(num):
    sum = 0
    divs = [x for x in range(1,num+1) if num % x == 0]
    mults = [x for x in divs if x % 3 == 0 or x % 5 == 0]
    for x in mults:
        sum += x
    return sum

print getDivs(1000)