def solution(s):
    alpha = {}
    answer = []
    
    for i, alp in enumerate(s):
        
        if alp not in alpha:
            answer.append(-1)
            
        else:
            answer.append(i - alpha[alp])
            
        alpha[alp] = i
    
    return answer