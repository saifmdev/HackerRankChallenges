from calendar import isleap
import itertools
import math
import os
import random
import re
import sys

# Easy

def weird_no_weird(num):
    if num % 2 != 0 or (num % 2 == 0 and num in range(6, 21)):
        print("Weird")
    elif num % 2 == 0 and (num in range(2, 6) or num > 20):
        print("Not Weird")

# TESTS
# print(weird_no_weird(10))
# print(weird_no_weird(22))
########################################################
# Easy, leapyear checker

def is_leap(year):
    leap = True if (year % 4 == 0 and year %
                    400 == 0 and year % 100 != 0) else False

    return leap

# TESTS
# print(isleap(2400))
# print(isleap(1992))
########################################################
# Easy

def print_range(num):
    arr = [str(x) for x in range(1, num + 1)]
    return ''.join(arr)


# TESTS
# print_range(5)
# print_range(3)
########################################################
# Easy

def square_array(n):
    arr = [x**2 for x in range(n)]
    for a in range(len(arr)):
        print(arr[a])


# TESTS
# square_array(5)
# square_array(8)
########################################################
# Easy - List Comprehension

def lexicographic(x, y, z, n):
    print([[i, j, k]
           for i in range(x+1)
           for j in range(y+1)
           for k in range(z+1) if (i+j+k) != n])

# TESTS
# lexicographic(1, 2, 1, 3)
# lexicographic(6, 6, 2, 8)
########################################################
#Easy - Sports Day Runner Up Score

def runner_up(n,arr):
    return max(list(filter(lambda a: a != max(arr), arr)))
    
#TESTS    
print(runner_up(5,[2,3,6,6,5]))