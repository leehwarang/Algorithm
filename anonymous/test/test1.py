def solution(arr):
    first = 0
    second = 1
    answer = []
    for i in range(len(arr)-1):
        if arr[first] == arr[second]:
            arr.remove(arr[second])
            answer.append(arr[first])
        else:
            first += 1
            second += 1
    first = 0
    second = 1
    for i in range(len(answer)-1):
        if answer[first] == answer[second]:
            answer.remove(answer[second])
        else:
            first += 1
            second += 1 
    return answer
    
print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4,4,4,3,3]))
print(solution([1,2,3,4]))