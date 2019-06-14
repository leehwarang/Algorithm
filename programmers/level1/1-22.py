'''
Prorgammers level1
문제: x만큼 간격이 있는 n개의 숫자
'''

def solution(x, n):
    answer = []
    count = 0
    sum = 0 
    while count < n:
        sum += x 
        answer.append(sum)
        count += 1 
    return answer