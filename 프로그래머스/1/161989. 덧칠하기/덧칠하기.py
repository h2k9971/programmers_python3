def solution(n, m, section):
    answer = 0
    i = 0 
    
    while i < len(section):
        
        answer += 1
        start = section[i]
        end = start + m - 1
        
        while i < len(section) and section[i] <= end:
            i += 1
        
    return answer