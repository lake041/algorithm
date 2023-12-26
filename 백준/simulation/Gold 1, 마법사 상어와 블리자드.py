# https://www.acmicpc.net/problem/21611
# 토네이도 좌표 순서만 구하면 된다

from sys import stdin
input = stdin.readline

def destroy():
    return

def explode():
    return

def copy():
    return

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
(sy, sx) = (N//2, N//2)
magics = []
for _ in range(M):
    d, s = map(int, input().split())
    magics.append((d-1, s))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

direction_list = []
for i in range(1, N):
    if i%2 == 1:
        for _ in range(i):
            direction_list.append(0)
        for _ in range(i):
            direction_list.append(1)
    if i%2 == 0:
        for _ in range(i):
            direction_list.append(2)
        for _ in range(i):
            direction_list.append(3)
for _ in range(N-1):
    direction_list.append(0)

order = []
(ty, tx) = (sy, sx)
for direction in direction_list:
    ty, tx = sy+dy[direction], sx+dx[direction]
    order.append((ty, tx))

'''
1: 0 1
2: 22 33
3: 000 111
4: 2222 3333
5: 00000 11111
6: 222222 333333
+ 000000
'''

answer = [0, 0, 0, 0]
for magic in magics:
    d, s = magic
    destroy(d, s)
    explode()
    copy()
print(answer[1]*1 + answer[2]*2 + answer[3]*3)