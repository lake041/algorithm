from itertools import product

def solution(board):
    answer = 0

    row_len = len(board)
    col_len = len(board[0])

    for row, col in product(range(1, row_len), range(1, col_len)):
        if board[row][col] == 0:
            continue
        board[row][col] = min(
            1 + board[row-1][col],
            1 + board[row][col-1],
            1 + board[row-1][col-1],
        )
        answer = max(answer, board[row][col]**2)

    return answer