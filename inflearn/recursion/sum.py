#1부터 n까지의 합

#재귀 활용
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(4))

#재귀 x
def sum2(n):
    result = 0 
    for i in range(1, n+1):
        result += i
    return result

print(sum2(5))


    