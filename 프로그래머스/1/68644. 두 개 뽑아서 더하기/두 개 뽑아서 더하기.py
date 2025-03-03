def solution(numbers):
    answer = []
    count = len(numbers)
    
    for i in range(count - 1):
        for j in range(i + 1, count):
            new_num = numbers[i] + numbers[j]
            
            if new_num not in answer:
                answer.append(new_num)
                
    answer = sorted(answer)
    
    return answer