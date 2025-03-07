def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
        
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer