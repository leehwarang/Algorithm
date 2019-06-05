# https://www.acmicpc.net/problem/5585

total = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

answer = 0

if total > 500:
    for coin in coins:
        answer += (total // coin)
        total = total % coin
elif total < 500 and total > 100:
    for coin in coins[1:]:
        answer += (total // coin)
        total = total % coin
elif total < 100 and total > 50:
    for coin in coins[2:]:
        answer += (total // coin)
        total = total % coin
elif total < 50 and total > 10:
    for coin in coins[3:]:
        answer += (total // coin)
        total = total % coin
elif total < 10 and total > 5:
    for coin in coins[4:]:
        answer += (total // coin)
        total = total % coin
else:
    answer = 1

print(answer)
