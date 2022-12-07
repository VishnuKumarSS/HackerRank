#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def check(strings):
    stack = []
    for i in strings:
        if i == '(':
            stack.append(10)
        elif i == ')':
            if len(stack) > 0 and stack[-1] == 10:
                stack.pop()
            else:
                return 1
        if i == '[':
            stack.append(20)
        elif i == ']':
            if len(stack) > 0 and stack[-1] == 20:
                stack.pop()
            else:
                return 1
        if i == '{':
            stack.append(30)
        elif i == '}':
            if len(stack) > 0 and stack[-1] == 30:
                stack.pop()
            else:
                return 1

    if len(stack) == 0:
        return 0
    else:
        return 1


def isBalanced(s):
    if check(s) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        fptr.write(result + '\n')

    fptr.close()
