from itertools import product

def solution(board):
    answer = 0
    width = len(board[0])
    height = len(board)

    def check(sy, sx, size):
        for row, col in product(range(sy, sy+size), range(sx, sx+size)):
            if board[row][col] == 0:
                return False
        return True

    
    for sy, sx in product(range(height), range(width)):
        if board[sy][sx] == 0:
            continue
        for size in range(1, min(height-sy, width-sx)+1):
            if check(sy, sx, size):
                answer = max(answer, size)
            
    return answer**2