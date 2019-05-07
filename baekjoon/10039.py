# 10
# 65
# 100
# 30
# 95

import sys

arr = []
for _ in range(5):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40
    arr.append(score)

print(sum(arr) // 5)