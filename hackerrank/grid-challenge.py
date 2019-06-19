# https://www.hackerrank.com/challenges/grid-challenge/problem

import math
import os
import random
import re
import sys


# Complete the gridChallenge function below.
def gridChallenge(grid):
    answer = ["" for i in range(len(grid[0]))]

    for i in range(len(grid)):
        grid[i] = "".join(sorted(grid[i]))

    for a in range(len(answer)):
        for g in range(len(grid)):
            answer[a] += grid[g][a]

    for i in range(len(answer)):
        if answer[i] != "".join(sorted(answer[i])):
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
