# 5
# OOXXOXXOOO -> 10
# OOXXOOXXOO -> 9
# OXOXOXOXOXOXOX -> 7
# OOOOOOOOOO -> 55
# OOOOXOOOOXOOOOX -> 30

n = int(input())


def OXquiz(inputStr):
    count = 0
    result = 0
    for i in inputStr:
        if i == 'O':
            count += 1
        else:
            count = 0
        result += count
    print(result)


for _ in range(n):
    inputStr = input()
    OXquiz(inputStr)
