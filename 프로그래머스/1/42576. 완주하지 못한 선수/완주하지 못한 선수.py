from collections import Counter

def solution(participant, completion):
    count = Counter(participant) - Counter(completion)
    answer = list(count.keys())[0]
        
    return answer