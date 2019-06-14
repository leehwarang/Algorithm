# https://www.hackerrank.com/challenges/priyanka-and-toys/problem

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the toys function below.
def toys(w):
    container = 1
    w.sort()
    unit = w[0] + 4
    w = w[1:]

    for i in range(len(w)):
        if w[i] > unit:
            container += 1
            unit = w[i] + 4

    return container


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
