#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    
       #python3

        numSwaps=0
        n=len(a)
        for i in range(n):
            for j in range(0, n-1-i):
                
                if a[j] > a[j+1]:
                    numSwaps+=1
                    a[j+1], a[j]=a[j], a[j+1]
                else:
                    pass
        last_element = a[-1]
        first_element = a[0]
        
        print(f'Array is sorted in {numSwaps} swaps.\nFirst Element: {first_element}\nLast Element: {last_element}')
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
