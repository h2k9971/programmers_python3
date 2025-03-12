def solution(numbers, target):
    answer = 0
    
    def dfs(index, current_sum):
        nonlocal answer
        
        if index == len(numbers):
            if current_sum == target:
                answer += 1

            return 
            
        dfs(index + 1, current_sum + numbers[index]) # 덧셈
        dfs(index + 1, current_sum - numbers[index]) # 뺄셈
    
    dfs(0, 0)
    
    return answer