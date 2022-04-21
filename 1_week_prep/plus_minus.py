#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos=neg=zero=c=0
    for item in arr:
        if item>0:
            pos+=1
            c+=1
        elif item<0:
            neg+=1
            c+=1
        else:
            zero+=1
            c+=1
    print("{:.6f}".format(pos/c))
    print("{:.6f}".format(neg/c))
    print("{:.6f}".format(zero/c))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

    
## Input:
# 6
# -4 3 -9 0 4 1

## Output
# 0.500000
# 0.333333
# 0.166667
