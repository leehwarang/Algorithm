base = [29, 10, 14, 37, 13]
first = 0
second = 1
n = len(base)
print(base)
for i in range(len(base)-1):
    first = 0
    second = 1
    for j in range(n-1):
        if base[first] > base[second]:
            temp = base[second]
            base[second] = base[first]
            base[first] = temp
        first += 1
        second += 1
        print(base)
    n -= 1


