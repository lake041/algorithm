from itertools import product
from collections import deque

N, M = map(int, input().split())
bod = [list(input()) for _ in range(N)]
chk = [[False]*M for _ in range(N)]

sy, sx = 0, 0
for y, x in product(range(N), range(M)):
    if bod[y][x] == "I":
        sy, sx = y, x
        chk[sy][sx] = True
        break

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ans = 0
q = deque()
q.append((sy, sx))
while q:
    y, x = q.popleft()
    for u, v in zip(dy, dx):
        ny, nx = y+u, x+v
        if 0<=ny<N and 0<=nx<M and chk[ny][nx]==False and bod[ny][nx]!='X':
            chk[ny][nx] = True
            q.append((ny, nx))
            if bod[ny][nx] == 'P':
                ans += 1
print(ans if ans > 0 else 'TT')

'''
3 5
OOOPO
OIOOX
OOOXP

1
'''