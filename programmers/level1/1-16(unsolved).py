'''
Prorgammers level1
문제: 소수 찾기
'''
import math

def solution(n):
    start = 2
    last = int(math.sqrt(n))
    base = list(range(2, last+1)) #입력받은 n이 이 배열에 있는 값들 중 나누어 떨어지는게 있다면 합성수, 없다면 소수

    for i in base:
        if n % i == 0:
            
    



solution(10)
solution(5)
#print(solution(10))
#print(solution(5))

# import math

# def solution(n):
#     base = list(range(2, n+1))
#     count = 0

#     for i in base: #2, 3, 4, 5
#         first = 2
#         last = math.sqrt(i)
        
#         if first > last:
#             count += 1

#         while first <= last: #나누는 값(first)이 루트 n보다 커지면 안됨
#             if i % first == 0:
#                 break
#             else:
#                 first += 1
#                 if first > last:
#                     count += 1
#                     break
#     return count


# print(solution(10))
# print(solution(5))

'''
import math

def solution(n):
    base = list(range(2, n+1))
    count = 0

    for i in base: #2, 3, 4, 5
        first = 2
        last = math.sqrt(i)
        
        if first > last:
            count += 1

        while first <= last: #나누는 값(first)이 루트 n보다 커지면 안됨
            if i % first == 0:
                break
            else:
                first += 1
                if first > last:
                    count += 1
                    break
    return count


print(solution(10))
print(solution(5))

'''

