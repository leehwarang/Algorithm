def solution(s):
      
    if len(s) == 4 or len(s) == 6:
        for i in s:
            try:
                int(i)
            except: 
                return False
        return True
    else:
        return False