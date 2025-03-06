def solution(k, tangerine):
    answer = 0
    total = 0
    dict = {}
    
    for size in tangerine:
        
        if size in dict:
            dict[size] += 1
        else:
            dict[size] = 1
    
    sorted_dict = sorted(dict.values(), reverse = True)
    
    for i in range(len(sorted_dict)):
        
        total = total + sorted_dict[i]
        answer += 1
        
        if total >= k:
            break
            
    return answer