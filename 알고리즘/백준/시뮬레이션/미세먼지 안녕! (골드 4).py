# Python: 시간 초과
# PyPy: 2644ms

from sys import stdin
from collections import defaultdict
from itertools import product
input = stdin.readline

R, C, T = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(R)]

purifier = [(y, x) for y, x in product(range(R), range(C)) if bod[y][x] == -1]
dust = [(y, x) for y, x in product(range(R), range(C)) if bod[y][x] >= 1]
(upper, _), (lower, _) = purifier[0], purifier[1]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def spread_dust(y, x, spread_result):
    targets = [(ny, nx) for u, v in zip(dy, dx) if 0<=(ny:=y+u)<R and 0<=(nx:=x+v)<C and bod[ny][nx]!=-1]
    each_amount = bod[y][x] // 5
    total_amount = each_amount * len(targets)

    for ty, tx in targets:
        spread_result[(ty, tx)] += each_amount
    spread_result[(y, x)] -= total_amount

def purify():
    for y in range(upper-1, -1, -1):
        bod[y+1][0] = bod[y][0]
    for x in range(0, C-1):
        bod[0][x] = bod[0][x+1]
    for y in range(0, upper):
        bod[y][C-1] = bod[y+1][C-1]
    for x in range(C-1, 0, -1):
        bod[upper][x] = bod[upper][x-1]

    for y in range(lower+1, R):
        bod[y-1][0] = bod[y][0]
    for x in range(0, C-1):
        bod[R-1][x] = bod[R-1][x+1]
    for y in range(R-1, lower, -1):
        bod[y][C-1] = bod[y-1][C-1]
    for x in range(C-1, 0, -1):
        bod[lower][x] = bod[lower][x-1]

    bod[upper][1], bod[lower][1] = 0, 0
    bod[upper][0], bod[lower][0] = -1, -1


for _ in range(T):
    spread_result = defaultdict(int)
    for y, x in product(range(R), range(C)):
        if bod[y][x] >= 1:
            spread_dust(y, x, spread_result)
    for (y, x), amount in spread_result.items():
        bod[y][x] += amount
    purify()

print(sum(bod[y][x] for y, x in product(range(R), range(C)) if bod[y][x] >= 1))