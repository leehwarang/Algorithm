'''
Prorgammers level1
문제: 문자열 다루기 기본(문자와 숫자 구별)
'''

def solution(s):
      
    if len(s) == 4 or 6:
        for i in s:
            try:
                float(s)
            except ValueError:
                return False
        return True
    else: 
        return False

solution("a234")
solution("1234")