# https://www.acmicpc.net/problem/1202

from heapq import heappop, heappush

N, K = map(int, input().split())
dias = sorted([list(map(int, input().split())) for _ in range(N)], reverse=True)
bags = sorted([int(input()) for _ in range(K)])
heapq = []

ans = 0
for bag in bags:
    while dias and dias[-1][0] <= bag:
        _, value = dias.pop()
        heappush(heapq, -value)
    ans += -heappop(heapq) if heapq else 0
print(ans)