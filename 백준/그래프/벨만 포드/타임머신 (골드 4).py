from sys import stdin, maxsize
from itertools import product
input = stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

def bellman_ford(start):
    dist = [maxsize]*(N+1)
    dist[start] = 0

    for round, edge in product(range(N), edges):
        cur, next_node, cost = edge
        new_dist = dist[cur] + cost
        if dist[cur] != maxsize and new_dist < dist[next_node]:
            dist[next_node] = new_dist
            if round == N-1:
                return dist, True
    return dist, False

dist, negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
    exit()

for i in range(2, N+1):
    print(-1 if dist[i] == maxsize else dist[i])