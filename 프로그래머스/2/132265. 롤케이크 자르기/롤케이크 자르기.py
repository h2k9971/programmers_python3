def solution(topping):
    answer = 0
    left_set = set()
    right_count = {}
    
    for t in topping:
        right_count[t] = right_count.get(t, 0) + 1
        
    for t in topping:
        left_set.add(t)
        right_count[t] -= 1
        
        if right_count[t] == 0:
            del right_count[t]
        
        if len(left_set) == len(right_count):
            answer += 1
    
    return answer