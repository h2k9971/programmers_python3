def solution(tickets):
    routes = {}
    for t in tickets:
        # 만약 t[0]이 이미 존재한다면 기존 리스트에 t[1]을 추가
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    
    for r in routes:
        routes[r].sort(reverse=True)
    
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            # 방금 추가한 목적지를 routes 에서 제거
            routes[top] = routes[top][:-1]
        
    return path[::-1]