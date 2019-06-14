'''
팰린드롬
'''

def solution(s):
    count = 0
    max_count = 0
    standard  = 0 

    for i, j in enumerate(s): 
        standard = i + 1
        print("기준 값:{0}".format(standard))
        if standard == len(s) - 1:
            break
        elif s[standard-1] == s[standard+1]:
            count = 0
            count += 1 
            print(count)
            for n in range(standard): #3번 반복 / n: 0 -> 1 -> 2
                print(n) #0
                if s[standard - (n+1)] ==  s[standard + (n+1)]:
                    count += 2
                    print(count)
                else:
                    break
            if count > max_count:
                max_count = count
                print("max_count:{0}".format(max_count))
        else:
            pass
    return max_count

#answer = solution("abcdcba")
#print("결과값:{0}".format(answer))

#answer = solution("abacde")
#print("결과값:{0}".format(answer))

answer = solution("akdidcbabcdn")
print("결과값:{0}".format(answer))

'''
만약 어떤 문자를 기준으로 전-후의 문자가 맞다면, 그 기준으로 잡은 문자가 가장 긴
팰린드롬을 만들 수 있다는 가정임. 그렇게 해서 count값을 뽑아낼 수는 있지만...
비교하다가 끝났을 때 바로 for문을 break시켜서 끝내는게 아니라.. max_count로 정하고 /
다음 문자열도 비교해야함.  
'''
