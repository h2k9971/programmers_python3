from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for order in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0
        
        for min_req, cost in order:
            if hp >= min_req:
                hp = hp - cost
                count += 1
            else:
                break
            
        max_count = max(max_count, count)
            
    return max_count