def solution(number):
    answer = 0
    
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                total_sum = 0
                total_sum = number[i] + number[j] + number[k]
                
                if total_sum == 0:
                    answer += 1
        
    return answer