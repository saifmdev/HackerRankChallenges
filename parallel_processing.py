import math
import os
import random
import re
import sys

# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#


def minTime(files, numCores, limit):
    total = 0
    for f in files:
        if limit <= numCores:
            if f % numCores == 0:
                total += (f/limit)
            else:
                total += f
        else:
            if f % numCores == 0:
                total += (f/numCores)
            else:
                total += f
                
    return int(total)

print(minTime([3,5,16,9], 3, 8))
print(minTime([5,3,1], 5, 5))