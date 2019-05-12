'''
처음에 배열의 마지막까지 순회했을 때, sum이 budget보다 작은 경우
return 해주는 값이 없어서 에러가 났었다..
'''

def solution(d, budget):
    d.sort()
    sum = 0
    answer = 0
    
    for i,j  in enumerate(d):
        sum += j
        if sum < budget:
            answer += 1
            if i == len(d) - 1:
                return answer
            
        elif sum == budget:
            answer += 1
            return answer
        else:
            return answer