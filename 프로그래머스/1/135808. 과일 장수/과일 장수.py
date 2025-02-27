def solution(k, m, score):
    total = 0
    box_num = len(score) // m
    new_box = []
    sorted_score = sorted(score, reverse = True)
    
    for i in range(box_num):
        new_box = sorted_score[i * m : m + i * m]
        min_score = min(new_box)
        total = total + m * min_score
        
    return total