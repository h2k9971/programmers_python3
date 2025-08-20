def solution(s):
    answer = 0
    same, diff = 0, 0
    x = s[0]
    
    for i, char in enumerate(s):
        if char == x:
            same += 1
        else:
            diff += 1
            
        if same == diff:
            answer += 1
            
            if i + 1 < len(s):
                x = s[i+1]
            same, diff = 0, 0
            
    if same != 0 or diff != 0:
        answer += 1
        
        
    return answer