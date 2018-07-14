'''
Prorgammers level1
문제: 행렬의 덧셈
'''

def solution(arr1, arr2):
    row_len = len(arr1)
    column_len = len(arr1[0])
    
    for i in range(row_len):
        for j in range(column_len):
            arr1[i][j] += arr2[i][j]
    return arr1

solution([[1,2],[2,3]], [[3,4],[5,6]])
solution([[1],[2]], [[3],[4]])