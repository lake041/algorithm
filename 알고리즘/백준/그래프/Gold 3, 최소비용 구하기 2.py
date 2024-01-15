# https://www.acmicpc.net/problem/11779
# 경로 출력

from heapq import heappush, heappop
from math import inf
from sys import stdin
input = stdin.readline

def dijkstra(start):
    global end
    distance = [inf]*(N+1)
    route = [[start] for _ in range(N+1)]
    heap = []
    heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        prev_cost, prev = heappop(heap)
        if distance[prev] < prev_cost:
            continue
        for next, cost in graph[prev]:
            next_cost = prev_cost + cost
            if next_cost < distance[next]:
                heappush(heap, [next_cost, next])
                route[next] = route[prev] + [next]
                distance[next] = next_cost

    return distance[end], route[end]

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
start, end = map(int, input().split())

minimum_cost, route = dijkstra(start)
print(minimum_cost)
print(len(route))
print(*route)


'''
https://www.acmicpc.net/board/view/118455
속도 줄이는 게 목적이면 필요하지만 그냥 다 탐색할 생각이라 크게 의미는 없는 듯
2
2
1 2 0
1 2 10
1 2
정답: 0

2
3
1 2 5
1 2 10
1 2 3
1 2
정답: 3

1
1
1 1 1
1 1
정답: 0
'''