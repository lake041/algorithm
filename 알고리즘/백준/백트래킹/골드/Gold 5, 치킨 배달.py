from sys import maxsize
from itertools import combinations, product

N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicks = []
for cy, cx in product(range(N), range(N)):
    num = bod[cy][cx]
    if num == 1:
        houses.append((cy, cx))
    if num == 2:
        chicks.append((cy, cx))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# memo[(cy, cx, hy, hx)] = distance
memo = {}
for cy, cx in chicks:
    for hy, hx in houses:
        memo[(cy, cx, hy, hx)] = abs(cy-hy) + abs(cx-hx)

ans = maxsize
for new_chicks in combinations(chicks, M):
    dist_sum = 0
    for hy, hx in houses:
        dist_sum += min([memo[(cy, cx, hy, hx)] for cy, cx in new_chicks])
    ans = min(ans, dist_sum)
print(ans)
