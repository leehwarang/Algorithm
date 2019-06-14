'''
Prorgammers level1
문제: 약수의 합
'''

def solution(n):
    answer = 0
    a = list(range(1, n+1))
    for i in a:
        if n % i == 0:
            answer += i 
    return answer

print(solution(12))
print(solution(5))