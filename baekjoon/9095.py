memo = {0:0, 1:1, 2:2, 3:4}
def sum123(n):
    if n not in memo.keys():
        return sum123(n-1) + sum123(n-2) + sum123(n-3)
    return memo[n]

a = int(input())
for _ in range(a):
    n = int(input())
    print(sum123(n));
    



