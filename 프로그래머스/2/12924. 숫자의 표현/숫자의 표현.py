def solution(n):
    answer = 0
    
    for i in range(n):
        total = 0

        for j in range(i + 1, n + 1):
            
            total = total + j
            if total > n:
                break
                
            if total == n:
                answer += 1
                break
        
    return answer