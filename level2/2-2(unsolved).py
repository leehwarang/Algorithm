'''
Prorgammers level2
문제: 행렬의 곱셈
'''

# arr1 = [[1,4], [3,2], [4,1]]
# arr2 = [[3, 3], [3, 3]]

# print(arr1 * arr2)

# 3행 2열(m x n)
# arr1[0][0]
# arr1[0][1]

# arr1[1][0]
# arr1[1][1]

# arr1[2][0]
# arr1[2][1]

# 2행 2열(n x p)
# arr2[0][0]
# arr2[0][1]
# arr2[1][0]
# arr2[1][1]

#mxn = nxk일 때 행렬의 곱셈이 성립하고, 결과는 mxk가 나온다.

def solution(arr1, arr2):
    matrix = []

    m = len(arr1) #arr1의 행의 개수
    n1 = len(arr1[0]) #arr2의 열의 개수

    n2 = len(arr2) #arr1의 행의 개수
    k = len(arr2[0]) #arr2의 열의 개수
    
    num = 0
    
    
    for i in range(m): #3번 반복(arr1의 행 개수만큼 반복) #0, 1, 2
        answer = [] #matrix에 더할 하나의 행 초기화
        sum = 0
        for j in range(k): #2번 반복(arr2의 열의 개수만큼 반복) 0, 1
            sum += (arr1[i][j] * arr2[i][j])
        print(sum)
        
        
        #answer.append(sum)
            
            

    
        #      + (arr1[i][i+1] * arr2[i+1][i])
        #     b = (arr1[i][i] * arr2[i][i+1]) + (arr1[i][i+1] * arr2[i+1][i+1])

        #     answer.append(a)
        #     answer.append(b)

        # matrix.append(answer)
    
    print(matrix)
    


solution([[1,4], [3,2], [4,1]], [[3, 3], [3, 3]])
    
