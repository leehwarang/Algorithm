from operator import itemgetter

def solution(arr1, arr2):
    arr1_dict = {} #딕셔너리는 중복 키 값을 저장할 수 없기 때문에 이 경우에 알맞음
    arr2_dict = {}
    for index, value in enumerate(arr1):
        arr1_dict[value] = arr1.count(value)
    for index, value in enumerate(arr2):
        arr2_dict[value] = arr2.count(value)

    print(arr1_dict)
    print(arr2_dict)
    
    #딕셔너리의 value값을 기준으로 정렬한 튜플을 반환함
    sorted_arr1 = sorted(arr1_dict.items(), key=(lambda x: x[1]), reverse = True)
    sorted_arr2 = sorted(arr2_dict.items(), key=(lambda x: x[1]), reverse = True)
    
    print(sorted_arr1)
    print(sorted_arr2)
    
    arr1_fair = sorted_arr1[0][1]
    arr2_fair = sorted_arr2[0][1]
    
    if arr1_fair == arr2_fair:
        if arr1_fair == 1:
            return 0
        elif sorted_arr1[0][0] > sorted_arr2[0][0]:
            return 1
        else:
            return 2
    elif arr1_fair > arr2_fair: #arr1 페어가 큰 경우
        return 1
    elif arr1_fair < arr2_fair: #arr2 페어가 큰 경우
        return 2  
    else:
        return 0

# print(solution([1, 5, 7, 2, 9], [2, 3, 9, 4, 8]))
print(solution([1, 4, 1, 3, 5], [9, 2, 3, 1, 3]))
# print(solution([1, 1, 9, 4, 1], [2, 3, 3, 9, 9]))
# print(solution([1, 4, 9, 4, 1], [9, 3, 1, 9, 1]))
