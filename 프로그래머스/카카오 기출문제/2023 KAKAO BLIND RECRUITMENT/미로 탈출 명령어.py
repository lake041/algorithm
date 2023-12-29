# 실패, 구글링 풀이
# DFS를 공부할 떄가 온 건가

from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

# 사전 순: Down, Left, Right, UP
D = {
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
}

def solution(R, C, sy, sx, ty, tx, k):
    sy, sx, ty, tx = map(lambda x: x-1, (sy, sx, ty, tx))
    dist = abs(ty-sy) + abs(tx-sx)
    if dist>k or (k-dist)%2==1:
        return 'impossible'
    
    ans = "z"
    
    def dfs(y, x, prev_routes, cnt):
        nonlocal ans
        if abs(ty-y)+abs(tx-x)+cnt > k:
            return
        if (y, x)==(ty, tx) and cnt==k:
            ans = prev_routes
            return
        for d in ('d', 'l', 'r', 'u'):
            ny, nx = y+D[d][0], x+D[d][1]
            if 0<=ny<R and 0<=nx<C and prev_routes<ans:
                dfs(ny, nx, prev_routes+d, cnt+1)
                
    dfs(sy, sx, "", 0)

    return ans