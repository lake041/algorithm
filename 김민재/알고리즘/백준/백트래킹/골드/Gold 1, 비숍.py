# https://www.acmicpc.net/problem/1799

# 같은 대각선에 있는지 판단하는 함수
def not_collision(y, x, bishops):
    for bishop in bishops:
        by, bx = bishop
        if abs(by-y) == abs(bx-x):
            return False
    return True

def find_next(row, col, N):
    if col+2 < N:
        return row, col+2
    if (row+col) % 2 == 0:
        if (row+1) % 2 == 0:
            return row+1, 0
        else:
            return row+1, 1
    else:
        if (row+1) % 2 == 0:
            return row+1, 1
        else:
            return row+1, 0

def go(row, col, cnt, bishops):
    global ans1, ans2
    if row == N:
        if (row+col)%2 == 1:
            ans1 = max(ans1, cnt)
        else:
            ans2 = max(ans2, cnt)
        return
    
    ny, nx = find_next(row, col, N)
    if bod[row][col]==1 and not_collision(row, col, bishops):
        go(ny, nx, cnt+1, bishops+[(row, col)])
    go(ny, nx, cnt, bishops)

N = int(input())
bod = [list(map(int, input().split())) for _ in range(N)]
ans1, ans2 = 0, 0
go(0, 0, 0, [])
go(0, 1, 0, [])
print(ans1 + ans2)

'''
5
1 1 0 1 1
0 1 0 0 0
1 0 1 0 1
1 0 0 0 0
1 0 1 1 1
7

3
0 1 1
1 1 1
1 1 1
4

4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
6

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
8

10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
18
'''