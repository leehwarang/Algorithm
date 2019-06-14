'''
Prorgammers level1
문제: 올바른 괄호
'''

def solution(s):
    a = 0 
    for i in s:
        if i == "(":
            a += 1
        else:
            if a < 1:
                return False
            else:
                a -= 1
    if a == 0:
        return True
    else:
        return False

solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")