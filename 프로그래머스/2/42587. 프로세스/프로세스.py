def solution(priorities, location):
    answer = 0
    queue = []
    priory = priorities

    # 대기 중인 프로세스 만들기
    for i in range(len(priorities)):
        queue.append(i)
        
    i = 0
    
    while queue:
        
        P1 = priory.pop(0) 
        Q1 = queue.pop(0) # 실행 대기 큐에서 프로세스 빼기
        
        if priory and max(priory) > P1: # 더 높은 우선순위가 있다면 다시 큐에 넣기
            priory.append(P1)
            queue.append(Q1)
            continue
        
        if Q1 == location:
            answer = answer + 1
            break
        
        answer += 1 
        i += 1
        
    return answer