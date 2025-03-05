def solution(l, r):
    answer = []
    
    for num in range(l, r + 1):
        num_str = str(num)
        is_valid = True
        
        for digit in num_str:
            if digit != '0' and digit != '5':
                is_valid = False
                break
    
        if is_valid:
            answer.append(num)
    
    return answer if answer else [-1]