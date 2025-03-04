def solution(a, b, n):
    answer = 0
    num = n
    
    while num >= a:
        
        remain = num % a
        num = (num // a) * b  
        answer += num
        num = remain + num 
        
    return answer