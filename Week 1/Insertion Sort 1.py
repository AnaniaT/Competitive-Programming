#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    n -= 1
    lastEl = arr[n]
    if not n:
        print(' '.join([str(x) for x in arr]))
    while n:
        if arr[n-1] > lastEl:
            arr[n] = arr[n-1]
        else:
            arr[n] = lastEl
            print(' '.join([str(x) for x in arr]))
            break
        n -= 1
        print(' '.join([str(x) for x in arr]))
        
    if not n:
        arr[0] = lastEl
        print(' '.join([str(x) for x in arr]))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
