'''
Prorgammers level1
문제: 문자열 내 p와 y의 개수
'''
def solution(s):
    s = s.upper()
    
    if s.count("P") == s.count("Y"):
        return True
    elif s.count("P") == 0 and s.count("Y") == 0:
        return True
    else: 
        return False
    

solution("pPoooyY")
solution("Pyy")