stack = []
def Implestack(arr):
    if arr[0] == 'push':
        stack.append(int(arr[1]))
    elif arr[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            a = stack[-1]
            del stack[-1]
            print(a)
    elif arr[0] == 'size':
        print(len(stack))

    elif arr[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif arr[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

n = int(input())
for _ in range(n):
    arr = input().split(" ")
    Implestack(arr);
 
