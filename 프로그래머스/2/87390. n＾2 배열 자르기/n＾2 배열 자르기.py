def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        answer.append(max(i // n + 1, i % n + 1))
    
    return answer