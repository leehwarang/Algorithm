'''
Prorgammers level2
문제: 최솟값 만들기
'''

def solution(A,B):
    answer = 0
    A = sorted(A) #오름차순 정렬
    B = sorted(B, reverse = True) #내림차순 정렬
    
    index = 0
    for _ in range(len(A)):
        answer += A[index]*B[index]
        index += 1
    return answer
    
print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))