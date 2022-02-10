import math
import os
import random
import re
import sys

# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example
# There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is

# Function Description
# Complete the sockMerchant function in the editor below.
# sockMerchant has the following parameter(s):

#     int n: the number of socks in the pile
#     int ar[n]: the colors of each sock

# Returns

#     int: the number of pairs

# Input Format

# The first line contains an integer
# , the number of socks represented in .
# The second line contains space-separated integers, , the colors of the socks in the pile.

def sockMerchant(n, ar):
    sock_dictionary = {}
    total_pairs = 0
    for num in ar:
        sock_dictionary[num] = ar.count(num)
        list(filter(lambda a: a != num, ar))

    for key in sock_dictionary:
        if sock_dictionary[key] // 2 > 0:
            total_pairs += sock_dictionary[key] // 2

    return total_pairs



print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))