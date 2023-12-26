# https://www.acmicpc.net/problem/1504
# 다익스트라

from heapq import heappush, heappop
from math import inf
from sys import stdin
input = stdin.readline

# 다익스트라
# 출발노드부터 다른 모든 노드까지의 최단경로
def dijkstra(start):
    distance = [inf for _ in range(N+1)]
    heap = []
    heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        dist, num = heappop(heap)
        if distance[num] < dist:
            continue
        for i, j in graph[num]:
            cost = dist + j
            if cost < distance[i]:
                distance[i] = cost
                heappush(heap, [cost, i])
    return distance

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

a = dijkstra(1)
b = dijkstra(v1)
c = dijkstra(v2)

# 1-v1-v2-N vs 1-v2-v1-N
answer = min(a[v1]+b[v2]+c[N], a[v2]+c[v1]+b[N])

if answer == inf:
    print(-1)
else:
    print(answer)