# https://www.acmicpc.net/problem/1167
# 루트를 내가 직접 계산해야 되나?

from heapq import heappush, heappop
from math import inf
from sys import stdin
input = stdin.readline

def dijkstra(start):
    distance = [inf]*(V+1)
    heap = []
    heappush(heap, [0, start])
    distance[start] = 0

    while heap:
        prev_dist, prev = heappop(heap)
        if distance[prev] < prev_dist:
            continue
        for next, dist in graph[prev]:
            next_dist = prev_dist + dist
            if next_dist < distance[next]:
                heappush(heap, [next_dist, next])
                distance[next] = next_dist

    return distance

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    x = list(map(int, input().split()))
    start = x[0]
    for i in range(1, len(x), 2):
        if x[i] == -1:
            break
        end, dist = x[i], x[i+1]
        graph[start].append([end, dist])
        graph[end].append([start, dist])

x = dijkstra(1)
furthest_dist = 0
furthest_node = 0
for i in range(1, V+1):
    if x[i] == inf:
        continue
    if furthest_dist < x[i]:
        furthest_dist = x[i]
        furthest_node = i

y = dijkstra(furthest_node)
print(max([z for z in y if z != inf]))