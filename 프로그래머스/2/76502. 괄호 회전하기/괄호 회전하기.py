def solution(s):
    answer = 0
    double_s = 2 * s
    
    for x in range(len(s)):
        stack = []
        new_s = double_s[x : x + len(s)] 
        
        for i in range(len(s)):
            
            if stack and stack[-1] == '{' and new_s[i] == '}':
                stack.pop()
            elif stack and stack[-1] == '[' and new_s[i] == ']':
                stack.pop()
            elif stack and stack[-1] == '(' and new_s[i] == ')':
                stack.pop()
            else:
                stack.append(new_s[i])
            
        if len(stack) == 0:
            answer += 1
            
    return answer