base = [29, 10, 14, 37, 13]
print(base)
n = len(base)
for _ in range(len(base)-1):
    index = base.index(max(base[:n]))
    temp = base[n-1]
    base[n-1] = base[index]
    base[index] = temp
    n -= 1
    print(base)
