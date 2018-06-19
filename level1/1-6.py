'''
Prorgammers level1
문제: 나누어 떨어지는 숫자 배열 
'''

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return sorted(answer)

solution([5,9,7,10], 5)
solution([2,36,1,3], 1)
solution([3, 2, 6], 10)