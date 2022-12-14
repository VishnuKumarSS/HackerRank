#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    ans = -63 # because we are taking 7 elements and -9 is the least value that each element can have so 7 * -9 = -63. The least value should not be 0 because negative values are less than 0.
    for i in range(4):
        for j in range(4):
            total = arr[i][j]+ arr[i][j+1]+ arr[i][j+2]+ arr[i+1][j+1] + arr[+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            ans = total if total > ans else ans # comparing to get the higher value
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
