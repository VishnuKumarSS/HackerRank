#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#


def waiter(numbers, q):
    answers = []

    # to find the prime numbers
    prime = []
    i = 2
    while i <= 10000:
        count = 1
        for j in range(2, i//2+1):
            if i % j == 0:
                count += 1
        if count == 1:
            prime.append(i)
        i += 1

    answers = []
    A = []
    B = []

    for i in range(q):
        if i == 0:
            new = number
        else:
            new = A
            A = []

        for j in range(len(new)):
            x = new.pop()
            if x % prime[i] == 0:
                B.append(x)
            else:
                A.append(x)
        while B:
            answers.append(B.pop())

    while A:
        answers.append(A.pop())
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
