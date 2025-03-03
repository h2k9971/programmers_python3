def solution(arr, divisor):
    answer = []
    arr_sorted = sorted(arr)
    
    for i in range(len(arr_sorted)):
        if arr_sorted[i] % divisor == 0:
            answer.append(arr_sorted[i])
    
    if len(answer) == 0:
        answer = [-1]
        
    return answer