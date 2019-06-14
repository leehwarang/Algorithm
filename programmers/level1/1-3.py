'''
Prorgammers level1
문제: 가운데 글자 가져오기 
'''

def solution(s):
    if len(s) == 1: #한자리 수 일 때
        return s
    
    elif len(s) % 2 == 0: #짝수 
        start = 0
        end = len(s) - 1 
        middle = int((start+end)/2)
        return s[middle:middle+2]
        
    else: #홀수 
        start = 0
        end = len(s) - 1 
        middle = int((start+end)/2)
        return s[middle]

s = "abcde"
solution(s)
s = "qwer"
solution(s)