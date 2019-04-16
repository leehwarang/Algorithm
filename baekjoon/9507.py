memo = { 0:1, 1:1, 2:2, 3:4}

def kongFibo(n):
    if n not in memo.keys():
        memo[n] = kongFibo(n-1) + kongFibo(n-2) + kongFibo(n-3) + kongFibo(n-4)                                                                                                                                                                                                                                                                                                                                      
    return memo[n]

a = int(input())
for _ in range(a):
    n = int(input())
    print(kongFibo(n)); 
