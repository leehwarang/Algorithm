# https://www.acmicpc.net/problem/2920

arr = list(map(int, input().split()))

if arr[0] == 1:
    minValue = arr[0]
    answer = "ascending"
    for i in range(len(arr[1:])):
        if minValue < arr[1:][i]:
            minValue = arr[1:][i]
        else:
            answer = "mixed"
            break
else:
    maxValue = arr[0]
    answer = "descending"
    for i in range(len(arr[1:])):
        if maxValue > arr[1:][i]:
            maxValue = arr[1:][i]
        else:
            answer = "mixed"
            break
print(answer)