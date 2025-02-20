def solution(x, n):
    answer = []
    
    for i in range(1, n+1):
        num = x
        num = num * i
        answer.append(num)
        
    return answer