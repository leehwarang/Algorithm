'''
Prorgammers level1
문제: 시저 암호
'''

import string

def solution(s, n):
    answer = '' 
    index = 0
    lower_str = string.ascii_lowercase
    upper_str = string.ascii_uppercase
    
    for i in s:
        if i in lower_str:
            index = lower_str.find(i)
            if index == 25:
                index = -1
            index += n
            answer += lower_str[index]
        elif i in upper_str:
            index = upper_str.find(i)
            if index == 25:
                index = -1
            index += n
            answer += upper_str[index]
        else:
            answer += ' '

    return answer       

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))