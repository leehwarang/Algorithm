'''
Prorgammers level1
문제: 수박수박수박수박수?
'''

def solution(n):
    answer = ''
    a = list(range(1, n+1))
    for i in a:
        if i % 2 != 0:
            answer += '수'
        else: 
            answer += '박'
    return answer

print(solution(3))
print(solution(4))



