# 5 20
# 99 101 1000 0 97

import sys

person, area = map(int, sys.stdin.readline().split(" "))
arr = sys.stdin.readline().split(" ")

for i, j in enumerate(arr):
    arr[i] = int(j)

count = person * area
answer = []
for i in arr:
    if count > i:
        answer.append(-(count - i))
    elif count < i:
        answer.append(-(count - i))
    else:
        answer.append(0)

answerStr = ''

for i in answer:
    answerStr += str(i)
    answerStr += ' '
print(answerStr)
