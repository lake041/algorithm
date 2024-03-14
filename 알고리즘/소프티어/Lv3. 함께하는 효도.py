from sys import stdin
from itertools import product
from copy import deepcopy
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
friends = []
for _ in range(M):
    y, x = map(int, input().split())
    friends.append([y-1, x-1])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

fruits = []
moves_list = list(product((0, 1, 2, 3), repeat=3))

for moves in product(moves_list, repeat=M):
    visited = [[False]*N for _ in range(N)]
    dots = deepcopy(friends)
    fruit = 0
    
    for y, x in dots:
        visited[y][x] = True
        fruit += bod[y][x]

    for i in range(3):
        for j in range(M):
            y, x = dots[j]
            d = moves[j][i]
            ny, nx = y+dy[d], x+dx[d]
            
            if 0<=ny<N and 0<=nx<N:
                dots[j] = [ny, nx]
                if not visited[ny][nx]:
                    fruit += bod[ny][nx]
                    visited[ny][nx] = True

    fruits.append(fruit)

print(max(fruits))