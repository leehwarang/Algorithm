'''
Prorgammers level1
문제: 두 정수 사이의 합
'''

def solution(a, b):
    sum =  a
    distance = abs(a-b)
    
    if a <= b:
        for _ in range(distance):
            a +=  1
            sum += a 
        return sum          
    else:
        for _ in range(distance):
            a  -= 1
            sum += a
        return sum
            
print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))