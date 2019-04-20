# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

n = int(input())
arr = []
answer = []
for i in range(1, n + 1):
    a = input().split(" ")
    for index, value in enumerate(a):
        a[index] = int(value)
    arr.append(a)

for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:  #index가 0이라면
            arr[i][j] += arr[i - 1][j]
        elif j == i:  #index가 depth와 같다면
            arr[i][j] += arr[i - 1][j - 1]
        else:  #index가 1부터 denpth-1 사이에 있는 값이라면
            arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

print(max(arr[n - 1]))
