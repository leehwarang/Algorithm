n = int(input())
rgblist = []

for i in range(n):
    r, g, b = map(int, input().split(" "))
    rgblist.append([r,g,b])

dp = []
dp.append(rgblist[0])


temp = []
for i in range(1, n):
    a = min(dp[i-1][1], dp[i-1][2]) + rgblist[i][0] #r을 선택했을 때
    b = min(dp[i-1][0], dp[i-1][2]) + rgblist[i][1] #g를 선택했을 때
    c = min(dp[i-1][0], dp[i-1][1]) + rgblist[i][2] #b를 선택했을 때
    
    dp.append([a, b, c])

print(min(dp[-1]))

