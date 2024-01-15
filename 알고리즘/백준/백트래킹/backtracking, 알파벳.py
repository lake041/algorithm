# https://www.acmicpc.net/problem/1987
# PyPy3 통과

R, C = map(int, input().split())
bod = [list(input()) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ans = 0
def back(y, x, cnt, visited):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<R and 0<=nx<C and bod[ny][nx] not in visited:
            visited.add(bod[ny][nx])
            back(ny, nx, cnt + 1, visited)
            visited.remove(bod[ny][nx])
back(0, 0, 1, set([bod[0][0]]))
print(ans)