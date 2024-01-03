from sys import maxsize
from heapq import heappop, heappush

def dijkstra(start, graph, N):
    dist = [maxsize]*(N+1)
    dist[start] = 0

    q = []
    heappush(q, (dist[start], start))
    while q:
        acc_dist, stopover = heappop(q)
        if dist[stopover] < acc_dist:
            continue
        for next_node, plus_dist in graph[stopover]:
            new_dist = acc_dist + plus_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(q, (dist[next_node], next_node))

    return dist
