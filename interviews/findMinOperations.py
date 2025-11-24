#!/bin/python3

import math
import os
import random
import re
import sys



from collections import deque
# Complete the 'findMinOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def findMinOperations(s):
    """
    Greedy: insert missing expected characters from the cycle "abc".
    Returns minimal number of insertions.
    """
    cycle = "abc"
    p = 0           # next expected index in "abc"
    ops = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i] == cycle[p]:
            i += 1
            p = (p + 1) % 3
        else:
            # simulate inserting cycle[p]
            ops += 1
            p = (p + 1) % 3
    # finish any partial cycle
    ops += (3 - p) % 3
    return ops

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = findMinOperations(s)

    fptr.write(str(result) + '\n')

    fptr.close()
