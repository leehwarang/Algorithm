'''
Prorgammers level1
문제: 직사각형 별찍기
'''

a, b = map(int, input().strip().split(' '))
star = ""
for i in range(a):
    star += "*"
for i in range(b):
    print(star)