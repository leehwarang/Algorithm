'''
Prorgammers level1
문제: 최대공약수와 최소공배수

풀이: 
두 수를 곱한 값은 최대공약수와 최소공배수를 곱한값과 같다.
A*B = G*L
'''
from fractions import gcd

def solution(a, b):
    answer = []
    min, max = 0, 0
    min = gcd(a, b)
    max = a*b / min
    answer.append(min)
    answer.append(max)
    return answer 
   
solution(3, 12)
solution(2, 5)