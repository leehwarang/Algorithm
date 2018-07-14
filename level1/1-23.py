'''
Prorgammers level1
문제: 핸드폰 번호 가리기
'''

def solution(phone_number):
    length = len(phone_number)
    n = length - 4 #7
    a = ''
    for i in range(n):
        a += "*"
    z = phone_number[n:]
    return a+z


solution("01033334444")
solution("027778888")