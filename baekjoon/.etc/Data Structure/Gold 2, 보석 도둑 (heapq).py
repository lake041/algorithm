from collections import deque
from heapq import heappush, heappop

N, K = map(int, input().split())
dias = [list(map(int, input().split())) for _ in range(N)]
dias.sort(key = lambda x: (x[0], -x[1]))
dias = deque(dias)
bags = [int(input()) for _ in range(K)]
bags.sort()

heap = []
fixed = []

for bag in bags:
    if not dias and not heap:
        break
    while dias and dias[0][0] <= bag:
        m, v = dias.popleft()
        heappush(heap, (-v, m))
    if heap:
        minus_v, m = heappop(heap)
        fixed.append(-minus_v)

print(sum(fixed))

'''
4 4
2 1
2 2
2 3
2 4
1
1
2
2

ANS : 7
'''