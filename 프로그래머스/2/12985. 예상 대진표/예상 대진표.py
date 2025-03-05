def solution(n,a,b):
    answer = 0
    N = n
    max_num = max(a, b)
    min_num = min(a, b)

    while N >= 2:
        
        if min_num + 1 == max_num and max_num % 2 == 0:
            answer += 1 
            break
            
        N = N // 2
        
        if min_num % 2 == 1:
            min_num = min_num // 2 + 1
        else:
            min_num = min_num // 2
            
        if max_num % 2 == 1:
            max_num = max_num // 2 + 1
        else:
            max_num = max_num // 2
            
        answer += 1
        
    return answer