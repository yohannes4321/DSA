# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

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
    key = arr[-1]  # Last element to be inserted
    j = n - 2
    
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]  # Shift elements
        print(*arr)  # Print after each shift
        j -= 1
    
    arr[j + 1] = key  # Place key at correct position
    print(*arr)  # Print final sorted array

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
