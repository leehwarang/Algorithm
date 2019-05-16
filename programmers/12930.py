def solution(s):
    arr = []
    arr = s.split(" ")
    fullAnswer = ''
    for a in arr:
        answer = ''
        for i, j in enumerate(a):
            if i == 0:
                answer += j.upper()
            elif i % 2 == 0: #짝수번째 문자이면
                answer += j.upper()
            else: #홀수번째 문자이면
                answer += j.lower()
        fullAnswer += answer
        fullAnswer += ' '
    return fullAnswer[0:len(fullAnswer)-1]
        