'''
Prorgammers level1
문제: 문자열 내 마음대로 정렬하기 
'''

def solution(a, b):
            a = sorted(a)
            #print(a)
            answer = [] 
            answer2 = [] 

            for i in a:
                answer.append(i[b])

            answer = sorted(answer)
            #print(answer)
    
            for i in answer: 
                for j in a:
                    if j[b] == i:
                        answer2.append(j)
                        a.remove(j)

            return answer2
    
  
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
            
    
        
#         for i in a:
#             if i[b] == 
        
#         for i in a:
#             answer.append(i[b])
#         answer = sorted(answer) #a, e, u 
#         print(answer)
        
#         answer2 = []
        
#         for i in range(len(answer)): #0, 1, 2 
#             for j in a: #sun, bed, car 
#                 if j[b] == answer[i]: 
#                     answer2.append(j)
#                     print(answer2)
#             length = len(answer2)
#             print(length)
#             answer2[length:] = sorted(answer2[length:])
#             print(answer2)
#         return answer2