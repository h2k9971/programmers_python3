def solution(k, score):
    answer = []
    max_score = []
    
    for i in range(len(score)):
        max_score.append(score[i])
        sorted_max_score = sorted(max_score, reverse = True)[:k]
        answer.append(sorted_max_score[-1])   
        
    return answer