'''
Prorgammers level2
문제: 다음 큰 숫자
'''

def solution(n):
    
    binary = bin(n)

    print(binary)
    cnt = str(binary).count("1")
    print(cnt)

    second_cnt = 0
    num = n
    while 1: 
        num += 1
        print(num)
        second_binary = bin(num)
        print(second_binary)
        second_cnt = str(second_binary).count("1")
        print(second_cnt)
        if cnt == second_cnt:
            return num
        else:
            pass
         
print(solution(78))
print(solution(15))