def solution(arr, k):
    answer = []
    set_arr = list(dict.fromkeys(arr))  # 중복을 제거하면서 원래 순서 유지
    
    for i in range(min(k, len(set_arr))): 
        answer.append(set_arr[i])
    
    while len(answer) < k:  # k개가 안 되면 -1 추가
        answer.append(-1)
    
    return answer
        
    return answer