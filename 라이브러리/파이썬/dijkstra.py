from sys import maxsize
from heapq import heappop, heappush

def dijkstra(start, graph, N):
    distance = [maxsize]*(N+1)
    distance[start] = 0

    q = []
    heappush(q, (distance[start], start))
    while q:
        acc_dist, stopover = heappop(q)
        if distance[stopover] < acc_dist:
            continue
        for next_node, plus_dist in graph[stopover]:
            new_dist = acc_dist + plus_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q, (distance[next_node], next_node))

    return distance
