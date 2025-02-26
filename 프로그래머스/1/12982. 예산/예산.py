def solution(d, budget):
    answer = 0
    total = 0
    sorted_d = sorted(d)
    
    for i in sorted_d:
        total += i
        
        if budget < total:
            break
            
        answer += 1
                   
    return answer