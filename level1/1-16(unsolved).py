'''
Prorgammers level1
문제: 소수 찾기
'''

import math

def solution(n):
    base = list(range(2, n+1))
    count = 0

    for i in base: #2, 3, 4, 5
        if i == 2 or i == 3:
            count += 1
        else:
            first = 2
            last = math.sqrt(i) #2부터 루트 5(2.23)까지 
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




    # for i in a:

    #     #i는 2부터 2제곱근까지의 값들을 비교하면 됨...
    #     last = math.sqrt(i)
    #     first = 2
    #     while first >= last: #2>1.4
    #         if i == first and i % first == 0:
    #             count += 1
    #         e
    #         if i % first == 0: #n이 i로 나누어 떨어진다면
    #             break #소수가 아니다. 
    #         else: #n이 i로 나누어 떨어지지 않는다면
    #             pass
    #     while start >= last: #2 >= 1.4
    #         if i % start == 0:
    #             count += 1 
            
    #                 count += 1
    #                 break
    #         else:
    #             if i % last == 0:
    #                 break
    #             else: 
    #                 last += 1
    # return count





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