def solution(nums):
    answer = 0
    N = len(nums)
    
    set_nums = set(nums)
    answer = min(len(set_nums), N // 2)
    
    return answer