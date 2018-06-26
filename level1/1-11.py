'''
Prorgammers level1
문제: 문자열 내림차순으로 배치하기
'''

def solution(s):
    answer = ''
    upper_s = s.upper()
    real_answer = '' 

    for i, n in zip(s, upper_s):
        if i == n:
            answer += i
            s = s.replace(i, "")
    s = sorted(s, reverse=True)
    answer = sorted(answer, reverse=True)

    for i in s:
        real_answer += i
    for i in answer:
        real_answer += i
    
    return real_answer
    
print(solution("Zbcdefg"))