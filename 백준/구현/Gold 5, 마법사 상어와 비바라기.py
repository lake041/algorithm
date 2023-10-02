# https://www.acmicpc.net/problem/21610

from itertools import product
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

my = [-1, -1, 1, 1]
mx = [-1, 1, -1, 1]

def cloud_move(d, s):
    global cloud
    new_cloud = []
    for y, x in cloud:
        ny = (y + dy[d]*s) % N
        nx = (x + dx[d]*s) % N
        new_cloud.append((ny, nx))
    cloud = new_cloud

def cloud_rain():
    global cloud
    rainy_cell = []
    for y, x in cloud:
        bod[y][x] += 1
        rainy_cell.append((y, x))
    cloud = []
    return rainy_cell

def copy(rainy_cell):
    for y, x in rainy_cell:
        count = 0
        for u, v in zip(my, mx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<N and bod[ny][nx]>0:
                count += 1
        bod[y][x] += count

def cloud_create(rainy_cell):
    for y, x in product(range(N), repeat=2):
        if bod[y][x] < 2 or (y, x) in rainy_cell:
            continue
        bod[y][x] -= 2
        cloud.append((y, x))

def answer():
    ans = 0
    for y, x in product(range(N), repeat=2):
        ans += bod[y][x]
    print(ans)

for _ in range(M):
    d, s = map(int, input().split())
    cloud_move(d-1, s)
    rainy_cell = cloud_rain()
    copy(rainy_cell)
    cloud_create(rainy_cell)
answer()