# https://www.hackerrank.com/challenges/jim-and-the-orders/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import operator

# Complete the jimOrders function below.
def jimOrders(orders):
    answer = []
    dict = {}
    for i in range(len(orders)):
        answer.append(orders[i][0]+orders[i][1])
        dict[i] = answer[i]
    
    sorted_dict = sorted(dict.items(), key = operator.itemgetter(1))
    
    realAnswer = []
    str = ''
    for i in range(len(sorted_dict)):
        realAnswer.append(sorted_dict[i][0] + 1)
    return realAnswer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
