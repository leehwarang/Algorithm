def start(base):

    # push
    # front, back, size, empty, pop
    if len(base) == 2:  #명령어가 push라면
        queue.append(base[1])
    else:
        command = base[0]
        if command == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                num = queue[0]
                del queue[0]
                print(num)
        elif command == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif command == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
        elif command == 'size':
            print(len(queue))
        else:  #empty
            if len(queue) == 0:
                print(1)
            else:
                print(0)


queue = []
n = int(input())
for _ in range(n):
    base = input().split(" ")
    start(base)