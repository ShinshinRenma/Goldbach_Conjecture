# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:55:37 2022
Verify one of the Goldbach Conjecture: the positive integer number 
(greater than or equal to 4) within 2000 can be decomposed into the 
sum of two prime numbers. Every even number's expression forming is 
such as: 4=2+2, print 6 expressions per line.
@author: rlaym_000
"""

#-*-coding:utf-8-*-
import math
 
def prime(x):
    if x == 1:
        return False
    n = int(math.sqrt(x))
    for i in range(2, n+1):
        if x % i == 0:
            return False
    return True
 
def GC(n):
    k = 3      
    while k < n:
         t = n - k
         if t < k:
             break
         if prime(k) and prime(t):
             return k, t
         k += 2
 
n = int(input())
if n > 4:
    a,b = GC(n)
    print("{}={}+{}".format(n, a, b))
elif n == 4:
    print("{}={}+{}".format(4, 2, 2))