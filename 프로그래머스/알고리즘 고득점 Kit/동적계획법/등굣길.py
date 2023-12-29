# 자주하는 실수
# 입력받는 값은 x, y 순서

def solution(m, n, puddles):
    MOD = 1_000_000_007
    
    bod = [[0]*m for _ in range(n)]
    bod[0][0] = 1
    
    for x, y in puddles:
        if y-1 >= 0 and x-1 >=0:
            bod[y-1][x-1] = -1
    
    for y in range(n):
        for x in range(m):
            if bod[y][x]==0:
                U = bod[y-1][x] if y-1>=0 and bod[y-1][x]>=0 else 0
                L = bod[y][x-1] if x-1>=0 and bod[y][x-1]>=0 else 0
                bod[y][x] = (U+L)%MOD 
    
    return bod[-1][-1]