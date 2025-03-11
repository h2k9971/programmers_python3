def solution(s):
    answer = []
    
    i = 0
    while i < len(s):
        
        if s[i:i+4] == 'zero':
            answer.append(str(0))
            i = i + 4
        elif s[i:i+3] == 'one':
            answer.append(str(1))
            i = i + 3
        elif s[i:i+3] == 'two':
            answer.append(str(2))
            i = i + 3
        elif s[i:i+5] == 'three':
            answer.append(str(3))
            i = i + 5
        elif s[i:i+4] == 'four':
            answer.append(str(4))
            i = i + 4
        elif s[i:i+4] == 'five':
            answer.append(str(5))
            i = i + 4
        elif s[i:i+3] == 'six':
            answer.append(str(6))
            i = i + 3
        elif s[i:i+5] == 'seven':
            answer.append(str(7))
            i = i + 5
        elif s[i:i+5] == 'eight':
            answer.append(str(8))
            i = i + 5
        elif s[i:i+4] == 'nine':  
            answer.append(str(9))
            i = i + 4
        else:
            answer.append((s[i]))
            i = i + 1
            
    return int("".join(answer))
