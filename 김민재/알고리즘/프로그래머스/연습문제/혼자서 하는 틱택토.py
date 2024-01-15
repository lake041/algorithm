from itertools import product

'''
홀짝에 따른 개수가 안 맞을 때
빙고가 2개 이상인
O가 이겼는데 OX 개수가 같다면 X가 한 번 더 뒀다는 것
X가 이겼는데 O가 더 많다면 O가 한 번 더 뒀다는 것
'''

def end_check(bod):
    for row in bod:
        if row == ["O", "O", "O"]:
            o_win += 1
        if row == ["X", "X", "X"]:
            x_win += 1
    
    bod = list(map(list, zip(*bod[::-1])))
    for row in bod:
        if row == ["O", "O", "O"]:
            o_win += 1
        if row == ["X", "X", "X"]:
            x_win += 1

def solution(board):
    bod = [list(row) for row in board]
    answer = 1

    o_cnt, x_cnt = 0, 0
    for y, x in product(range(3), range(3)):
        if bod[y][x] == 'O':
            o_cnt += 1
        if bod[y][x] == 'X':
            x_cnt += 1
    total = o_cnt + x_cnt

    if total%2 == 0 and o_cnt != x_cnt:
        answer = 0
    if total%2 == 1 and o_cnt != x_cnt+1:
        answer = 0

    o_win, x_win = 0, 0
    for row in bod:
        if row == ["O", "O", "O"]:
            o_win += 1
        if row == ["X", "X", "X"]:
            x_win += 1
    
    bod = list(map(list, zip(*bod[::-1])))
    for row in bod:
        if row == ["O", "O", "O"]:
            o_win += 1
        if row == ["X", "X", "X"]:
            x_win += 1
    
    if [bod[0][0], bod[1][1], bod[2][2]] == ["O", "O", "O"]:
        o_win += 1
    if [bod[0][0], bod[1][1], bod[2][2]] == ["X", "X", "X"]:
        x_win += 1
    if [bod[0][2], bod[1][1], bod[2][0]] == ["O", "O", "O"]:
        o_win += 1
    if [bod[0][2], bod[1][1], bod[2][0]] == ["X", "X", "X"]:
        x_win += 1

    if o_win == 2 and o_cnt == 5:
        pass
    elif o_win + x_win > 1:
        answer = 0
    
    if o_win and o_cnt == x_cnt:
        answer = 0 

    if x_win and o_cnt != x_cnt:
        answer = 0 

    return answer