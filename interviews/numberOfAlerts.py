#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfAlerts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER precedingMinutes
#  2. INTEGER alertThreshold
#  3. INTEGER_ARRAY numCalls
#

def numberOfAlerts(precedingMinutes, alertThreshold, numCalls):
    if precedingMinutes <= 0:
        return 0
    n = len(numCalls)
    if precedingMinutes > n:
        return 0

    counter = 0
    # initial window: first `precedingMinutes` elements (for t = precedingMinutes-1)
    window = sum(numCalls[:precedingMinutes])

    # iterate windows that include current minute: first window ends at index precedingMinutes-1
    for end in range(precedingMinutes - 1, n):
        avg = window / precedingMinutes
        if avg > alertThreshold:    # strict "exceeds"
            counter += 1
        # slide window forward: remove element that leaves and add the next element (if any)
        next_idx = end + 1
        if next_idx < n:
            leave_idx = end - precedingMinutes + 1
            window -= numCalls[leave_idx]
            window += numCalls[next_idx]

    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    precedingMinutes = int(input().strip())

    alertThreshold = int(input().strip())

    numCalls_count = int(input().strip())

    numCalls = []

    for _ in range(numCalls_count):
        numCalls_item = int(input().strip())
        numCalls.append(numCalls_item)

    result = numberOfAlerts(precedingMinutes, alertThreshold, numCalls)

    fptr.write(str(result) + '\n')

    fptr.close()
