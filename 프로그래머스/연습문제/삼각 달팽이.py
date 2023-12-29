from collections import defaultdict

dy = [1, 0, -1]
dx = [0, 1, -1]

def solution(N):
    tri = [[0]*k for k in range(1, N+1)]
    visited = defaultdict(bool)
    
    if N == 1:
        return [1]
    
    num = 1
    y, x = 0, 0
    d = 0
    while True:
        tri[y][x] = num
        visited[(y, x)] = True
        num += 1
        
        ny, nx = y+dy[d], x+dx[d]
        if ny>=N or nx>=N or visited[(ny, nx)]:
            d = (d+1)%3
            ny, nx = y+dy[d], x+dx[d]

        y, x = ny, nx
        if visited[(ny, nx)]:
            break
    
    return [x for row in tri for x in row]

# 시간초과
'''
def solution(N):
    dp = {
        1: [[1]],
        2: [[1], [2, 3]],
        3: [[1], [2, 6], [3, 4, 5]]        
    }
    
    for i in range(4, N+1):
        end = (i-1)*3
        prev = dp[i-3]
        for index, row in enumerate(prev):
            prev[index] = [index+3] + [x+end for x in row] + [end-index-1]
        prev = [[1]] + [[2, end]] + prev + [[x for x in range(i, 2*i)]]
        dp[i] = prev
    
    return [num for row in dp[N] for num in row]
'''