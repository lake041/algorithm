from sys import stdin, maxsize
from itertools import product, combinations
input = stdin.readline

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
ans = maxsize

houses = [(y, x) for y, x in product(range(N), range(N)) if bod[y][x] == 1]
chicks = [(y, x) for y, x in product(range(N), range(N)) if bod[y][x] == 2]
memo = {key: [] for key in houses}

for (hy, hx), (cy, cx) in product(houses, chicks):
    distance = abs(hy-cy) + abs(hx-cx)
    memo[(hy, hx)].append((distance, (cy, cx)))

for values in memo.values():
    values.sort()

for chicks_combination in combinations(chicks, M):
    sub_dist = 0
    for (hy, hx) in houses:
        for distance, (cy, cx) in memo[(hy, hx)]:
            if (cy, cx) in chicks_combination:
                sub_dist += distance
                break
    ans = min(ans, sub_dist)

print(ans)

