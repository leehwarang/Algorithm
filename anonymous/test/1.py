def solution(s):
    s.sort()
    answer = 0
    dict = {}
    for i in s:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    
    if 4 in dict.keys():
        answer += dict[4]
        del dict[4]
    
    if dict[1] == dict[3] and dict[1] + dict[3] <= 4:
        answer += dict[1] # dict[1] 또는 dict[3]의 개수 만큼 answer에 더하고
    elif dict[1] > dict[3]:
        answer += dict[3]
        answer += (dict[1] - dict[3])
    elif dict[1] < dict[3]:
        answer += dict[1]
        answer += (dict[3] - dict[1])
    elif dict[1] == dict[2] and dict[1] + dict[2] <=4 :
        answer += dict[1]
    elif dict[1] > dict[2]:
        answer += dict[2]
        answer += (dict[1] - dict[2])
    elif dict[1] < dict[2]:
        answer += dict[1]
        answer += (dict[2] - dict[1])
    answer += 1

    return answer

print(solution([1,2,4,3,3]))
print(solution([2,3,4,4,2,1,3,1])) 
# solution([3,3,3,2])