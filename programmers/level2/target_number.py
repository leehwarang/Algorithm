answer = 0

def DFS(numbers, target, index, sum):
    print("===index:{}, sum:{}===".format(index-1, sum))
    global answer
    if len(numbers) == index:
        if target == sum:
            print("성공")
            answer += 1
            return
            
        else:
            print("실패")
            return
    else:
        DFS(numbers, target, index+1, sum + numbers[index])
        DFS(numbers, target, index+1, sum - numbers[index])

def solution(numbers, target):
    global answer
    DFS(numbers, target, 0, 0)
    return answer

arr = [1,1,1,1,1]
target = 3

print(solution(arr, target))