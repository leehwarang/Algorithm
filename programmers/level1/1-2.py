'''
Prorgammers level1
문제: 같은 숫자는 싫어
'''


def solution(arr):
    answer = []

    for i, v in enumerate(arr):
        if i == 0:
            answer.append(v)
        elif arr[i] == arr[i - 1]:
            pass
        else:
            answer.append(v)
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))

arr = [4, 4, 4, 3, 3]
print(solution(arr))