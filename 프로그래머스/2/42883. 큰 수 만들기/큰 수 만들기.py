def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and num > collected[-1] and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer