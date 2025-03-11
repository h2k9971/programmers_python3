def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            
            if i == j:
                continue
                
            mul = numbers[i] * numbers[j]
            answer.append(mul)
    
    return max(answer)