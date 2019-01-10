'''
=====
2573번: 빙산
=====
input:
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
=====
output:
2
=====
'''

str = input('빙산의 행과 열을 입력하세요. :');
a = str.split(' ')
n, m = int(a[0]), int(a[1]) #n은 빙산의 행, m은 빙산의 열을 의미함

iceburg = [];

for i in range(n):
    str = input("{}번 째 행을 입력하세요.".format(i))
    dummy = str.split(' ')
    for i, j in enumerate(dummy):
        dummy[i] = int(j)
    iceburg.append(dummy)

print("=====빙하기 시작 전=====")
print(iceburg)

print("=====빙하기 시작=====")

years = 0

cnt_main_list = []
for i in range(1, n-1):
    cnt_list = []
    for j in range(1, m-1):
        cnt = 0
        if iceburg[i-1][j] == 0:
            cnt += 1
        if iceburg[i][j+1] == 0:
            cnt += 1
        if iceburg[i+1][j] == 0:
            cnt += 1
        if iceburg[i][j-1] == 0:
            cnt += 1
        cnt_list.append(cnt)
    cnt_main_list.append(cnt_list)

print(cnt_main_list) #주위 빙하의 계산은 잘됨.

#두 개의 이차원 배열(iceburg, cnt_main_list 끼리 뺄셈 해야함.)

for i in range(1, n-1):
    for j in range(1, m-1):
        

    # print(cnt_list)
    # for j,k in zip(range(1, m-1), cnt_list):
    #     iceburg[i][j] -= k
    #     if iceburg[i][j] - k <= 0:
    #        iceburg[i][j] = 0
    #     else: 
    #         iceburg[i][j] -= k

years += 1

print("=====1년 후=====")
print(iceburg)




# b = [][]
# for(int i=0; i<n; i++) {
#     input
#   b[i] = str.split(' ');
# }






