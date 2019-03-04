base = [15, 12, 13, 10, 14, 11]
print("정렬 전 배열: {}".format(base))

for i in range(1, (len(base))):
    temp = base[i]
    n = i - 1
    print("{}({})를 정렬합니다.".format(temp, i))
    while n == 0 or n > 0: #temp와 비교하는 값의 인덱스가 0이 될 때까지
        
        if temp < base[n]:
            base[n+1] = base[n]
            n -= 1
        else: #비교해나가다가 들어갈 공간을 찾은 경우
            base[n+1] = temp
            break
    if n < 0:
        base[n+1] = temp #0번째 인덱스 값까지 비교했을 때 
    print(base)