from sys import maxsize

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(bod, aloc, bloc):
    R, C = len(bod), len(bod[0])

    def is_finished(y, x):
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<R and 0<=nx<C and bod[ny][nx]:
                return False
        return True

    def solve(y1, x1, y2, x2): # 1번 차례
        if is_finished(y1, x1):
            return [False, 0] # can_win, turn, 내가 움직일 곳이 없으면 진다

        if y1==y2 and x1==x2:
            return [True, 1] # 겹쳐있을 때 움직이면 이긴다

        min_turn = maxsize
        max_turn = 0
        can_win = False

        for u, v in zip(dy, dx):
            ny, nx = y1+u, x1+v
            if not(0<=ny<R and 0<=nx<C) or not bod[ny][nx]:
                continue

            bod[y1][x1] = 0
            result = solve(bod, y2, x2, ny, nx) # 2번 차례
            bod[y2][x2] = 1

            if not result[0]: # 이 시점에서는 result[0]이 False여야만 현재 턴에서 내가 이길 수 있다.
                can_win = True
                min_turn = min(min_turn, result[1])
            elif not can_win:
                max_turn = max(max_turn, result[1])

        turn = min_turn if can_win else max_turn

        return [can_win, turn + 1]

    return solve(bod, aloc[0], aloc[1], bloc[0], bloc[1])[1]