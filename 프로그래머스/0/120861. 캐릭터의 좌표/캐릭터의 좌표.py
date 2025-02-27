def solution(keyinput, board):
    x, y = 0, 0
    max_x = board[0] // 2
    max_y = board[1] // 2

    move = {"up" : (0, 1), "down" : (0, -1), "left": (-1, 0), "right" : (1, 0)}
    
    for key in keyinput:
            
        dx, dy = move[key]
        x, y = x + dx, y + dy 
        
        x = max(-max_x, min(max_x, x))
        y = max(-max_y, min(max_y, y))
    
    return [x, y]