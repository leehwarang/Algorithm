# #방법1
# answer = 0
# def DFS(numbers, target, index, sum):
#     global answer
    
#     if(index == len(numbers)):
#         if target == sum:
#             answer += 1
#             return
#         else:
#             return

#     DFS(numbers,target, index + 1, sum+numbers[index])
#     DFS(numbers,target, index + 1, sum-numbers[index])
# def solution(numbers, target):
#     global answer
#     DFS(numbers,target,0,0)
#     return answer

# print(solution([1,1,1,1,1], 3))

#방법2

def dfs(numbers, target, index, sum):
    if index==len(numbers):
        return (1 if sum==target else 0)
    return dfs(numbers, target, index+1, sum+numbers[index])+dfs(numbers, target, index+1, sum-numbers[index])

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer

print(solution([1,1,1,1,1],3))