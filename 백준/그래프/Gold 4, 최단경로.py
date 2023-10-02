# https://www.acmicpc.net/problem/1753

from heapq import heappush, heappop
from math import inf
from sys import stdin
input = stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    distance = [inf]*(V+1)
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, num = heappop(heap)
        if distance[num] < dist:
            continue
        for i, j in graph[num]:
            new_dist = dist + j
            if new_dist < distance[i]:
                heappush(heap, (new_dist, i))
                distance[i] = new_dist
    return distance

result = dijkstra(start)
for i in range(1, V+1):
    print('INF' if result[i]==inf else result[i])