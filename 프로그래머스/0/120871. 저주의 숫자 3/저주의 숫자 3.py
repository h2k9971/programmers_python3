def solution(n):
    answer = 0
    start_num = 0
    
    while start_num < n:
        answer = answer + 1
        
        if answer % 3 == 0 or '3' in str(answer):
            continue
            
        start_num += 1
                
    return answer