# Python: 1244ms
# PyPy: 432ms

from sys import stdin
from itertools import product
input = stdin.readline

R, C, T = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(R)]

purifier = [(y, x) for y, x in product(range(R), range(C)) if bod[y][x] == -1]
dust = [(y, x) for y, x in product(range(R), range(C)) if bod[y][x] >= 1]
(upper, _), (lower, _) = purifier[0], purifier[1]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

targets = [[0]*C for _ in range(R)]
numbers = [[0]*C for _ in range(R)]
for y, x in product(range(R), range(C)):
    targets[y][x] = [(ny, nx) for u, v in zip(dy, dx) if 0<=(ny:=y+u)<R and 0<=(nx:=x+v)<C and bod[ny][nx]!=-1]
    numbers[y][x] = len(targets[y][x])

def spread_dust(bod, targets, numbers):
    new_bod = [[0]*C for _ in range(R)]
    new_bod[upper][0], new_bod[lower][0] = -1, -1

    for y, x in product(range(R), range(C)):
        if bod[y][x] <= 0:
            continue
        each_amount = bod[y][x] // 5
        left_amount = bod[y][x] - each_amount * numbers[y][x]

        for ty, tx in targets[y][x]:
            new_bod[ty][tx] += each_amount
        new_bod[y][x] += left_amount

    return new_bod

def purify(bod):
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
    bod = spread_dust(bod, targets, numbers)
    purify(bod)

print(sum(sum(row) for row in bod) + 2)