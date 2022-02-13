import math
import os
import random
import re
import sys


# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    result = []
    for query in queries:
        arr = numbers[query[0]-1:query[1]]
        map(lambda x: x if x != 0 else query[2], arr)
        result.append(sum(arr))
    return result



print(findSum([0,3,9,5],[[1,2],[2,3]]))
