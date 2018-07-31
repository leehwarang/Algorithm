'''
Prorgammers level1
문제: 자연수 뒤집어 배열로 만들기
'''

def solution(n):
    str_n = str(n)
    answer = []
    for i in list(reversed(str_n)):
        answer.append(int(i))
    return answer

solution(12345)