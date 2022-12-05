#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#


def twoStacks(maxSum, a, b):
    a.reverse()
    b.reverse()
    stack = []
    running_sum = 0
    step = 0

    while a:
        item = a.pop()
        if (running_sum + item) <= maxSum:
            running_sum += item
            step += 1
            stack.append(item)
        else:
            break

    step_answer = step

    while b:
        item = b.pop()
        running_sum += item
        step += 1
        # In below while loop we are removing some steps that we did in the list a.
        while running_sum > maxSum and stack:
            running_sum -= stack.pop()
            step -= 1
        if running_sum <= maxSum and step > step_answer:
            step_answer = step

    return step_answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
