'''
Prorgammers level2
문제: 최댓값과 최솟값
'''

def solution(s):
    answer = s.split(" ")
    for i,j in enumerate(answer):
        answer[i] = int(answer[i])
    answer = sorted(answer)
    min = answer[0]
    max = answer[-1]

    return "{0} {1}".format(min, max)
    

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))

