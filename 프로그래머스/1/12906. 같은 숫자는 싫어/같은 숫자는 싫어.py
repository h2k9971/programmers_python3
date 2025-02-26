def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        
        if i < 1:
            answer.append(arr[i])
            
        elif arr[i - 1] == arr[i]:
            continue
            
        else:
            answer.append(arr[i])

    return answer