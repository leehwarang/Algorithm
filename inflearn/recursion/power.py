
def double_power(x, n):
    if n == 0:
        return 1
    else:
        return x * double_power(x, n-1)

print(double_power(2,3))
print(double_power(3,4))
