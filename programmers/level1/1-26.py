'''
Prorgammers level1
문제: 하샤드 수
'''

def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if x % sum == 0:
        return True
    else:
        return False


solution(10)
solution(12)
solution(11)
solution(13)