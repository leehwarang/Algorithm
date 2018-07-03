'''
Prorgammers level1
문제: 소수 찾기
'''

'''
n의 약수를 발견하면 소수가 아니고(=합성수 이고)
n의 약수를 발견하지 못하면 소수이다.

이 때 2부터 (n-1)번째의 숫자까지 비교하면서 나누어 떨어지는게 있는지 검사하는게 아니라, 
2부터 n의 제곱근까지 비교하면서 나누어 떨어지는게 있는지 검사하면 된다.

'''

import math

def solution(n):
    a = list(range(2, n+1))
    count = 0
    for i in a:

        #i는 2부터 2제곱근까지의 값들을 비교하면 됨...
        last = math.sqrt(i)
        first = 2
        while first >= last: #2>1.4
            if i == first and i % first == 0:
                count += 1
            e
            if i % first == 0: #n이 i로 나누어 떨어진다면
                break #소수가 아니다. 
            else: #n이 i로 나누어 떨어지지 않는다면
                pass
        while start >= last: #2 >= 1.4
            if i % start == 0:
                count += 1 
            
                    count += 1
                    break
            else:
                if i % last == 0:
                    break
                else: 
                    last += 1
    return count


print(solution(10))
print(solution(5))


# def solution(n):
#     a = list(range(2, n+1))
#     count = 0
#     for i in a:
#         divide = 2
#         while i >= divide: #2>=2, 3>=2, 3>=3, 4>=2,
#             if i == divide and i % divide == 0: 
#                     count += 1
#                     break
#             else:
#                 if i % divide == 0:
#                     break
#                 else: 
#                     divide += 1
#     return count


# print(solution(10))
# print(solution(5))