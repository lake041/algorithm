dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(board, aloc, bloc):
    R, C = len(board), len(board[0])
    visited = [[False]*C for _ in range(R)]

    def solve(cury, curx, opy, opx):
        if visited[cury][curx]:
            return 0

        ret = 0 # 처음부터 못 움직인다면 A의 패배, 짝수는 A의 패배, 홀수는 B의 패배

        for u, v in zip(dy, dx):
            ny, nx = cury+u, curx+v

            if not(0<=ny<R and 0<=nx<C) or visited[ny][nx] or board[ny][nx] == 0:
                continue

            visited[cury][curx] = True
            val = solve(opy, opx, ny, nx)+1
            visited[cury][curx] = False 
            
            if ret % 2 == 0 and val % 2 == 1: ret = val # 바로 갱신
            elif ret % 2 == 0 and val % 2 == 0: ret = max(ret, val) # 최대한 늦게 지는걸 선택
            elif ret % 2 == 1 and val % 2 == 1: ret = min(ret, val) # 최대한 빨리 이기는걸 선택

        return ret

    return solve(aloc[0], aloc[1], bloc[0], bloc[1])