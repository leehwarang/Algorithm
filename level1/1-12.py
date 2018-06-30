'''
Prorgammers level1
문제: 서울에서 김서방 찾기
'''

def solution(seoul):
    count = 0
    
    for i in seoul:
        if i == "Kim":
            text = "김서방은 {0}에 있다".format(count)
            return text
        else:
            count += 1

seoul = ["Jane", "Kim"]
print(solution(seoul))
