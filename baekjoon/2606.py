# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

data = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
queue = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    data[a][b] = 1
    data[b][a] = 1

cnt = 0
queue.append(1)
visited[1] = 1

while (not len(queue) == 0):
    column = queue.pop(0)

    for i in range(len(data[column])):
        if data[column][i] == 1 and visited[i] == 0:
            queue.append(i)
            visited[i] = 1
            cnt += 1
print(cnt)