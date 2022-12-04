#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#


def getMax(operations):
    arr = []
    stack_ans = []
    ans = []

    # to split the string values in a array to array of array values - to make less time complex code
    splitted_array = []
    for i in operations:
        element = i.split(" ")
        splitted_array.append(element)

    # working part
    for splitted in splitted_array:
        if splitted[0] == "1":
            value = int(splitted[1])
            arr.append(value)
            if len(stack_ans) == 0 or stack_ans[-1] < value:
                stack_ans.append(value)
            else:
                stack_ans.append(stack_ans[-1])
        elif splitted[0] == "2":
            arr.pop()
            stack_ans.pop()
        else:
            ans.append(stack_ans[-1])
        # print(stack_ans)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
