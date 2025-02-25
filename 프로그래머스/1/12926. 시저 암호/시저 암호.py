def solution(s, n):

        
    answer = []
    
    for char in s:
    
        if char.isupper():
            answer.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        elif char.islower():
            answer.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        else:
            answer.append(char)
    
    return ''.join(answer)