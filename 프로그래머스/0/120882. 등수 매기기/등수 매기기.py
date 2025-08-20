def solution(score):
    averages = []
    
    for a, b in score:
        averages.append((a+b) / 2)
    
    answer = []
    
    for avg in averages:
        rank = 1
        for other in averages:
            if other > avg:
                rank = rank + 1
        answer.append(rank)
    
    return answer