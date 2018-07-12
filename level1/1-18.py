'''
Prorgammers level1
문제: 짝수와 홀수
'''

def solution(num):
    
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(solution(3))
print(solution(5))