# memo = {0: 0, 1: 1}

# def fibo(n):
#     if n not in memo:
#         memo[n] = fibo(n - 1) + fibo(n - 2)
#     return memo[n]


def solution(n):
    fibo = [0, 1]

    for i in range(2, n + 1):
        fibo.append(fibo[i - 2] + fibo[i - 1])

    return fibo[-1] % 1234567
