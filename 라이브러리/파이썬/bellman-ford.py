from sys import maxsize
from itertools import product

def bellman_ford(start, edges, N):
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