from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    
    heap = []
    for i in range(len(scoville)):
        heappush(heap, scoville[i])
        
    while heap[0] < K:
        
        if len(heap) == 1:
            answer = -1
            break
            
        min1 = heappop(heap)
        min2 = heappop(heap)
        
        new_heap = min1 + min2 * 2
        heappush(heap, new_heap)
        
        answer += 1
    
    return answer