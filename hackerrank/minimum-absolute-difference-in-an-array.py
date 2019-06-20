# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    answer = []
    length = len(answer)

    for i in range(len(arr)):
        if i == len(arr) - 1:
            break
        if arr[i] < 0 and arr[i+1] < 0:
            first = - arr[i]
            second = - arr[i+1]
        else:
            first = arr[i]       
            second = arr[i+1]
        answer.append(abs(first-second))
    
    return min(answer)

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()