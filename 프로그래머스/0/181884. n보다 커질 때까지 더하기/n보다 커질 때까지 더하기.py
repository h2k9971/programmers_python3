def solution(numbers, n):
    answer = 0
    total = 0
    
    for i in range(len(numbers)):
        total = total + numbers[i] 
        
        if total > n:
            break
        
    return total