# 101111
# 101010
# 101011
# 111011

import sys

x, y = map(int, sys.stdin.readline().split())
data = [[0]*y for _ in range(x)]

for i in range(x):
    temp = sys.stdin.readline();
    for j in range(y):
        data[i][j] = int(temp[j])

# print(data)

visited = [[0] * y for _ in range(x)]

# print(visited)

dx = [0,0,-1,1] #상, 하, 좌, 우
dy = [-1,1,0,0] #상, 하, 좌, 우

queue = []
queue.append((0,0)) # 출발 지점을 queue에 넣는다. 
visited[0][0] = 1 

while (queue): 
    a, b = queue.pop(0) # queue에 있는 원소를 뺀다. 
    if a == (x-1) and b == (y-1): # 종료 조건
        print(visited[a][b])
        break

    for i in range(4): # queue에서 pop한 원소의 인접 원소들을 탐색한다. 
        ax = a + dx[i]
        ay = b + dy[i]
        
        if ax >= 0 and ax < x and ay >= 0 and ay < y:
            if visited[ax][ay] == 0 and data[ax][ay] == 1: # 아직 방문하지 않았고, 갈 수 있는 원소라면
                visited[ax][ay] = visited[a][b] + 1
                queue.append((ax,ay)) 
                # print(queue)
    

            

    
    






