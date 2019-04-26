# 10 5
# 1 10 4 9 2 3 8 5 7 6

#1 4 2 3

a, x = map(int, input().split(" "))
arr = input().split(" ")
answer = []

for i, j in enumerate(arr):
    arr[i] = int(j)

for i in arr:
    if i < x:
        answer.append(i)
answerStr = ''
for i in answer:
    answerStr += str(i)
    answerStr += ' '
print(answerStr)
