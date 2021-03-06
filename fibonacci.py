#!/usr/bin/env python2.7
"""
Even Fibonacci Numbers
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci
sequence whose values do not exceed four million, find the sum of the
even-valued terms.

Author: Dan Granillo <dan.granillo@gmail.com>

"""

def genFibs(upperlim):
    fibs = []
    fib = 0
    fib1 = 0
    fib2 = 1
    for i in range(1, upperlim+1):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        fibs.append(fib)
    return fibs
    
def filterFibs(seq):
    evenFibs = [i for i in seq if i % 2 == 0 and i <= 4000000]
    return evenFibs

def sumFibs(seq):
    sumFibs = 0
    for i in seq:
        sumFibs += i
    print sumFibs

print sumFibs(filterFibs(genFibs(1000)))