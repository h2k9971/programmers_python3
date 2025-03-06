def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    
    if len(stack) == 0:
        answer = True
        
    return len(stack) == 0