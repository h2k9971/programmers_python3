from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps) # row의 개수
    m = len(maps[0]) #column의 개수
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque([(x, y)])
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    # 이동 거리 기록하기 (누적으로)
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        
        if maps[n-1][m-1] > 1:
            answer = maps[n-1][m-1]
        else:
            answer = -1
            
        return answer
    
    return bfs(0, 0)