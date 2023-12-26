def solution(bod):
    bod = [row + [0] for row in bod]
    H = [0]*len(bod[0])
    nemo = []

    for row in bod:
        H = [prev+1 if now else 0 for prev, now in zip(H, row)]
        stack = [(-1, 0)]
        for index, height in enumerate(H):
            while stack and height < stack[-1][1]:
                h = stack.pop()[1]
                w = index - stack[-1][0] - 1
                nemo.append(min(h, w))
            stack.append((index, height))
    
    return max(nemo)**2 if nemo else 0

# from itertools import product

# def solution(board):
#     answer = 0

#     row_len = len(board)
#     col_len = len(board[0])
    
#     if row_len==1 and col_len==1 and board[0][0]==1:
#         return 1

#     for row, col in product(range(1, row_len), range(1, col_len)):
#         if board[row][col] == 0:
#             continue
#         board[row][col] = min(
#             1 + board[row-1][col],
#             1 + board[row][col-1],
#             1 + board[row-1][col-1],
#         )
#         answer = max(answer, board[row][col]**2)

#     return board