#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diverseDeputation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER w
#

def diverseDeputation(m, w):
    # Write your code here
    if m == 0 or w == 0:
        return 0
    
    answer = 0
    answer += m * (w * (w - 1) // 2)
    answer += w * (m * (m - 1) // 2)
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input().strip())

    w = int(input().strip())

    result = diverseDeputation(m, w)

    fptr.write(str(result) + '\n')

    fptr.close()