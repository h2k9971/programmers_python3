from collections import deque

def solution(board, moves):
    answer = 0
    stack_basket = []
    move = deque(moves)
    
    while move:
        
        column = move.popleft() - 1
        for row in range(len(board)):
            
            if board[row][column] == 0:
                continue
                
            else:
                new_doll = board[row][column]
                    
                if stack_basket and stack_basket[-1] == new_doll:
                    stack_basket.pop()
                    answer += 2
                else:
                    stack_basket.append(new_doll)
                    
                board[row][column] = 0
                break
        
    return answer