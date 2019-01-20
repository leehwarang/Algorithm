'''
최대 공약수: Euclid Method

'''

def gcd(m, n):
    if n > m:
        temp = m
        m = n
        n = temp

    if m % n == 0:
        return n
    else:
        return gcd(n, m-n) 

print(gcd(18, 12))
print(gcd(12, 18))