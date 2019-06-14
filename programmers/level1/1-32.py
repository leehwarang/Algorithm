#두 정수 사이의 합
def sum(x, y):
    sum = 0
    for i in range(x, y+1):
        sum += i
    return sum
    
def solution(a, b):
    result = sum(a, b) if a == b or a<b else sum(b,a)

    return result
    
print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
