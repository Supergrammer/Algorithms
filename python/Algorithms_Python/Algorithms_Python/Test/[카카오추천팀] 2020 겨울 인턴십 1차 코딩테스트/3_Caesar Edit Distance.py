#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'editDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING source
#  2. STRING target
#

def editDistance(source, target):
    # Write your code here
    most = [0] * 26
    source = list(map(ord, list(source)))
    target = list(map(ord, list(target)))
    
    for i in range(len(source)):
        tmp = source[i] - target[i]
        if tmp < 0: tmp += 26

        most[tmp] += 1
        
    mx = 0
    for i in range(26):
        if most[i] > mx: mx = most[i]
           
    return (len(source) - mx) * 2
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    source = input()

    target = input()

    result = editDistance(source, target)

    fptr.write(str(result) + '\n')

    fptr.close()