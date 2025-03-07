import math 

def solution(progresses, speeds):
    answer = []
    date = []
    
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        date.append(day)
    
    i = 0
    while i < len(date):
        count = 1
        
        for j in range(i + 1, len(date)):
        
            if date[i] >= date[j]:
                count += 1
            else:
                break
                
        answer.append(count)
        i += count
    
    return answer