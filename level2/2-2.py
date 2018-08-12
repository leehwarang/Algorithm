'''
Prorgammers level2
문제: 행렬의 곱셈
'''

def solution(A, B):
    answer2 = []
    for A_row in A: #A의 행 개수만큼 반복
        answer = []
        for B_col in zip(*B): #B 행렬을 전치 시키고 첫 번째 행만 내보냄. B의 행 개수만큼 반복 
            sum = 0
            print(A_row)
            print(B_col)
            for a, b in zip(A_row, B_col): #안에 있는 원소의 개수만큼 반복
                sum += a*b
            answer.append(sum)
        answer2.append(answer)
    return answer2
        
print(solution([[1,2], [2,3]], [[3,4],[5,6]]))
print(solution([[1,4], [3,2], [4,1]], [[3, 3], [3, 3]]))
print(solution([[2,3,2], [4,2,4], [3,1,4]], [[5,4,3], [2,4,1], [3,1,1]]))

#참고한 사이트: http://d4m0n.tistory.com/48


#numpy 사용
'''
import numpy as np

def solution(arr1, arr2):
    
    array1 = np.array(arr1)
    array2 = np.array(arr2)

    return (np.dot(array1, array2)).tolist()

print(solution([[1,4], [3,2], [4,1]], [[3, 3], [3, 3]]))
print(solution([[2,3,2], [4,2,4], [3,1,4]], [[5,4,3], [2,4,1], [3,1,1]]))
'''


#실패한 코드들
'''
def solution(arr1, arr2):
    matrix = []

    m = len(arr1) #arr1의 행의 개수
    n1 = len(arr1[0]) #arr2의 열의 개수

    n2 = len(arr2) #arr2의 행의 개수
    k = len(arr2[0]) #arr2의 열의 개수
    
    num = 0

    for i in range(m): #3번 반복(arr1의 행 개수만큼 반복) #0, 1, 2
        answer = [] #matrix에 더할 하나의 행 초기화
        sum = 0
        for _ in range(k):
            for j in range(k): #2번 반복(arr2의 열의 개수만큼 반복) 0, 1
                sum += (arr1[i][j] * arr2[j][i]) #arr1의 첫 번째 행과 arr2의 첫 번째 열 /
            answer.append(sum)

        
        
        answer.append(sum)
            
             + (arr1[i][i+1] * arr2[i+1][i])
            b = (arr1[i][i] * arr2[i][i+1]) + (arr1[i][i+1] * arr2[i+1][i+1])

            answer.append(a)
            answer.append(b)

        matrix.append(answer)
    
    print(matrix)
    
    solution([[1,4], [3,2], [4,1]], [[3, 3], [3, 3]])
    '''
    
