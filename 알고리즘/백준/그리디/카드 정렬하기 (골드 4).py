from heapq import heapify, heappop, heappush

N = int(input())
cards = [int(input()) for _ in range(N)]
heapify(cards)

ans = 0

for _ in range(N-1):
    a = heappop(cards)
    b = heappop(cards)
    heappush(cards, a + b)
    ans += a + b

print(ans)