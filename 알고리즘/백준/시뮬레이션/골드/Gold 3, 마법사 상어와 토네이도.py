# https://www.acmicpc.net/problem/20057
# 검색한 풀이 참고해서 우아하게 풀어보려고 했는데 이해가 안 돼서 기존 풀이만 약간 개선함

from sys import stdin
input = stdin.readline

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

N = int(input())
bod = [list(map(int, input().split())) for _ in range(N)]

'''
0: 0 1
1: 22 33
2: 000 111
3: 2222 3333
4: 00000 11111
5: 222222 333333
6: 000000
'''

direction_list = []
for i in range(N-1):
    if i%2 == 0:
        for j in range(i+1):
            direction_list.append(0)
        for j in range(i+1):
            direction_list.append(1)
    if i%2 == 1:
        for j in range(i+1):
            direction_list.append(2)
        for j in range(i+1):
            direction_list.append(3)
for j in range(N-1):
    direction_list.append(0)

def move(tornado, d):
    global answer
    y, x = tornado
    total = bod[y][x]
    spreads = 0
    bod[y][x] = 0

    cells = [
        (y+dy[(d+2)%4]+dy[(d+3)%4], x+dx[(d+2)%4]+dx[(d+3)%4], 1), # 1%
        (y+dy[(d+2)%4]+dy[(d+1)%4], x+dx[(d+2)%4]+dx[(d+1)%4], 1), # 1%
        (y+dy[(d+3)%4]+dy[(d+3)%4], x+dx[(d+3)%4]+dx[(d+3)%4], 2), # 2%
        (y+dy[(d+1)%4]+dy[(d+1)%4], x+dx[(d+1)%4]+dx[(d+1)%4], 2), # 2%
        (y+dy[d]+dy[d], x+dx[d]+dx[d], 5), # 5%
        (y+dy[(d+3)%4], x+dx[(d+3)%4], 7), # 7%
        (y+dy[(d+1)%4], x+dx[(d+1)%4], 7), # 7%
        (y+dy[d]+dy[(d+3)%4], x+dx[d]+dx[(d+3)%4], 10), # 10%
        (y+dy[d]+dy[(d+1)%4], x+dx[d]+dx[(d+1)%4], 10), # 10%
        (y+dy[d], x+dx[d], 0) # @
    ]

    for cell in cells:
        y, x, ratio = cell
        spread = int(total*ratio/100)
        if ratio == 0:
            if 0<=y<N and 0<=x<N:
                bod[y][x] += total - spreads
            else:
                answer += total - spreads
        else:
            spreads += spread
            if 0<=y<N and 0<=x<N:
                bod[y][x] += spread
            else:
                answer += spread

answer = 0
tornado = [N//2, N//2]
for direction in direction_list:
    y, x = tornado
    tornado = [y+dy[direction], x+dx[direction]]
    move(tornado, direction)
print(answer)