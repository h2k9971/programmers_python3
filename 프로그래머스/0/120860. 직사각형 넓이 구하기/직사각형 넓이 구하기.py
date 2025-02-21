def solution(dots):
    answer = 0
    x = []
    y = []
    
    for dot in dots:
        for i in range(len(dot)):
            if i == 0:
                x.append(dot[i])
            else:
                y.append(dot[i])
    
    answer = (max(x) - min(x)) * (max(y) - min(y))
    
    return answer