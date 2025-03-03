def solution(s):
    answer = True
    p_num = 0
    y_num = 0
    
    for i in range(len(s)):
        
        if s[i] == 'P' or s[i] == 'p':
            p_num += 1
            
        elif s[i] == 'Y' or s[i] =='y':
            y_num += 1
        
    if p_num == y_num:
        answer = True
        
    else:
        answer = False 
    return answer