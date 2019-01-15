#1. 재귀를 이용한 피보나치 수열

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))


#2.DP를 이용한 피보나치 수열

memo = {1:1, 2:1}

def fib(n):
    if n<=2:
        return 1
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
