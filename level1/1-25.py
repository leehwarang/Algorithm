'''
Prorgammers level1
문제: 제일 작은 수 제거하기
'''

def solution(arr):
    length = len(arr)
    min = arr[0]
    for i in range(length): 
        if i == length-1:
            break
        elif min > arr[i+1]:
            min = arr[i+1]
        else:
            pass
    arr.remove(min)
    if len(arr) == 0: #첫 번째 원소가 가장 작았기 때문에 삭제해서 빈 배열이 됨.
        return [-1]
    else:
        return arr

solution([4,3,2,1])
solution([10])