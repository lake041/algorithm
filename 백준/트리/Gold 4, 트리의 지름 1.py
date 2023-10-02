# https://www.acmicpc.net/problem/1967
# 감 살짝 잡았나 싶었는데 시간초과
# 처음 방식으로 하면 1만^2 = 1억 번의 다익스트라를 수행해야 함
# O(ElogE) -> 1만 x 1만 x 4 = 4억 -> 4초 : 절반만 줄일 수 있을까
# 지름이 되는 간선은 특정 노드를 미드로 가지는 간선들 중 최대 거리에 위치한 간선을 포함할 것이고
# 루트 노드는 해당 노드를 반드시 지나기 때문에
# 루트 노드에서의 최대 거리에 위치한 간선은 반드시 트리의 지름 중 한 쪽 끝을 반드시 포함한다
# 논리 문제였네
# 정정 -> 루트가 아니어도 무조건 포함함

from heapq import heappush, heappop
from math import inf
from sys import stdin
input = stdin.readline

def dijkstra(start):
    distance = [inf]*(N+1)
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

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

x = dijkstra(1)
furthest_node = 0
furthest_dist = 0
for i in range(1, N+1):
    if x[i] == inf:
        continue
    if furthest_dist < x[i]:
        furthest_node = i
        furthest_dist = x[i]

y = dijkstra(furthest_node)
print(max([z for z in y if z != inf]))