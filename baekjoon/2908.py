import sys

arr = sys.stdin.readline().split(" ")
x = arr[0]
y = arr[1]

realX = ''
realY = ''
for i in x[::-1]:
    realX += i

for j in y[::-1]:
    realY += j

realX = int(realX)
realY = int(realY)

if realX > realY:
    print(realX)
else:
    print(realY)