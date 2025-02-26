def solution(seoul):

    i = 0
    
    for name in seoul:
        if name == 'Kim':
            answer = f"김서방은 {i}에 있다"
            break
        i += 1
        
    return answer