import math
import os
import random
import re
import sys

# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
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