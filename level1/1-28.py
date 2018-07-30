'''
Prorgammers level1
문제: 정수 제곱근 판별
'''

import math

def solution(n):
    num = math.sqrt(n)
    if num % 1 == 0.0:
        return int((num+1)**2)
    else:
        return -1 

print(solution(121))
print(solution(3))