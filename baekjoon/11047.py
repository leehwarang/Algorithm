#입력 받은 동전 중 money보다 작거나 같지만 가장 큰 동전을 기준으로 둔다.
#money를 그 동전으로 나눈 값을 cnt에 더한다.
#money를 그 동전으로 나눈 나머지를 money로 하고, 1)부터 이 행동을 반복한다.
n, money = map(int, input().split(" "))
coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))

for coin in coins[::-1]:
    if money >= coin:
        start = coin
        break

index = coins.index(start)
coins = coins[:index+1]

for coin in coins[::-1]:
    num = (money // coin)
    money = money % coin
    cnt += num
print(cnt)

