def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        
        if signs[i] == 0:
            absolutes[i] = -absolutes[i]

        answer += absolutes[i]

    
    return answer