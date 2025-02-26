def solution(arr):
    answer = []
    min_num = min(arr)
    
    if arr == [10]:
        return [-1]
    
    for num in arr:
        
        if num == min_num:
            continue
        else:
            answer.append(num)
    
    return answer