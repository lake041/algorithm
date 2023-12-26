# https://it-garden.tistory.com/247

from itertools import product
from math import inf

N = int(input())
bod = [list(map(int, input().split())) for _ in range(N)]

floyd = [[inf]*N for _ in range(N)]
for y, x in product(range(N), range(N)):
    if bod[y][x] > 0:
        floyd[y][x] = bod[y][x]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if floyd[i][j] > floyd[i][k] + floyd[k][j]:
                floyd[i][j] = floyd[i][k] + floyd[k][j]

for y, x in product(range(N), range(N)):
    if floyd[y][x] != inf:
        floyd[y][x] = 1
    else:
        floyd[y][x] = 0

for row in floyd:
    print(*row)

'''
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
'''