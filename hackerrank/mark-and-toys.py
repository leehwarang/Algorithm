# https://www.hackerrank.com/challenges/mark-and-toys/problem

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    money = k
    prices.sort()
    answer = 0

    for i in range(len(prices)):
        money -= prices[i]
        if money > 0:
            answer += 1
        elif money == 0:
            answer += 1
            return answer
        else:
            return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()