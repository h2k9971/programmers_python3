def solution(numbers, k):
    answer = 0
    size = len(numbers)
    
    for i in range(k):
        
        if i == 0:
            continue
        else:
            answer = (answer + 2) % size
    
    return answer + 1