'''
Prorgammers level1
문제: 콜라츠 추측
'''

def solution(num):
    count = 0
    while count < 499:
        if num % 2 == 0:
            num = num / 2
            count +=1
            if num == 1:
                return count
        else:
            num = (num * 3) + 1
            count +=1
            if num == 1:
                return count     
    return -1
        
solution(6)
solution(16)
solution(626332)

