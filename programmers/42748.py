def solution(array, commands):
    answer = []
    temp = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
        temp = []
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])