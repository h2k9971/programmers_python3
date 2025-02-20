def solution(lines):
    
    dict = {}
    
    for i in range(len(lines)):
        point = lines[i]
        
        for num in range(point[0], point[1], 1):
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
                
    answer = 0
    for i in dict.values():
        if i >= 2:
            answer += 1

    return answer