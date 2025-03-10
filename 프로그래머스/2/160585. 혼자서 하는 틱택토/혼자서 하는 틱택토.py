def check_bingo(board, symbol):
    # 가로 빙고 확인
    for row in board:  
        if row == symbol * 3:
            return True
        
    # 세로 빙고 확인
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    
    # 대각선 빙고 확인
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    
    return False

def solution(board):
    answer = 1
    x_count = 0
    o_count = 0

    for i in range(len(board)):
        x_count += board[i].count('X')
        o_count += board[i].count('O')

    if x_count > o_count or o_count - x_count >= 2:
        return 0
   
    o_win = check_bingo(board, 'O')
    x_win = check_bingo(board, 'X')

    if o_win and x_win:
        return 0
        
    elif o_win and o_count != x_count + 1:
        return 0
        
    elif x_win and o_count != x_count:
        return 0
    else:
        answer = 1
        
    return answer