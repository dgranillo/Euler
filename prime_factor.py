#!/usr/bin/env python2.7
"""
Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor
of the number 600851475143 ?

Author: Dan Granillo <dan.granillo@gmail.com>

Note: Causes MemoryError on Cloud9 virtual machine. Test on VPS. Should work though..

"""
from math import sqrt
#is factor
def factor(number):
    factors = [i for i in range(1,number+1,2) if number % i == 0]
    return factors
#is prime
def prime(numbers):
    primes = []
    for each in numbers:
        factors = [i for i in range(2,int(sqrt(each))+1) if each % i == 0]
        if len(factors) > 0:
            continue
        else:
            primes.append(each)
    return primes
#print largest
def out(numbers):
    print numbers[len(numbers)-1]

out(prime(factor(475143)))
