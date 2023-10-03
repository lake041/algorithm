from itertools import product

def solution(board):
    answer = 0
    width = len(board[0])
    height = len(board)

    for sy, sx in product(range(height), range(width)):
        if board[sy][sx] == 0:
            continue
        for size in range(1, min(height-sy, width-sx)+1):
            possible = True
            
            row = sy+size-1
            for col in range(sx, sx+size):
                if board[row][col] == 0:
                    possible = False
                    break
            if not possible:
                break
                
            col = sx+size-1
            for row in range(sy, sy+size):
                if board[row][col] == 0:
                    possible = False
                    break
            if not possible:
                break
            
            answer = max(answer, size**2)
            
    return answer