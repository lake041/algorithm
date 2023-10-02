# https://www.acmicpc.net/problem/1916
# 이제 외울 때도 됐다

from heapq import heappush, heappop
from math import inf
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
start, end = map(int, input().split())

def dijkstra(start):
    cost = [inf]*(N+1)
    heap = []
    heappush(heap, (0, start))
    cost[start] = 0
    while heap:
        target_cost, target = heappop(heap)
        if cost[target] < target_cost:
            continue
        for i, j in graph[target]:
            new_cost = target_cost + j
            if new_cost < cost[i]:
                heappush(heap, (new_cost, i))
                cost[i] = new_cost
    return cost

print(dijkstra(start)[end])