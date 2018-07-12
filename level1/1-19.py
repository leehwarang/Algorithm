'''
Prorgammers level1
문제: 평균 구하기
'''

def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    average = answer / len(arr) 
    return average


print(solution([1,2,3,4]))
print(solution([5,5]))