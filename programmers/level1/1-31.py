'''
Prorgammers level1
문제: 이상한 문자 만들기

각 단어의 짝수번째 알파벳 -> 대문자
각 단어의 홀수번째 알파벳 -> 소문자

연속된 공백이 있는 경우...
'''

def solution(s):
    answer = ''
    text = []
    text = s.split(" ")
    for i in text:
        index = 0
        for j in i:
            if index == 0:
                answer += j.upper()
            elif index % 2 == 0: #짝수번째 문자이면
                answer += j.upper()
            else: #홀수번째 문자이면
                answer += j.lower()
            index += 1
        if index == text[-1]:
            pass
        else:     
            answer += " "
    return answer
                
print(solution("try hello world"))