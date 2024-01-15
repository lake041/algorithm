from sys import maxsize, stdin
from heapq import heappop, heappush
from collections import deque
input = stdin.readline

def dijkstra(N, graph, start):
    dist = [maxsize] * (N+1)
    dist[start] = 0
    path = [[] for _ in range(N+1)]

    q = [(0, start)]
    while q:
        acc_dist, stopover = heappop(q)
        for next_node, plus_dist in graph[stopover]:
            new_dist = acc_dist + plus_dist
            if new_dist == dist[next_node]:
                path[next_node].append(stopover)
            elif new_dist < dist[next_node]:
                dist[next_node] = new_dist
                path[next_node] = [stopover]
                heappush(q, (new_dist, next_node))

    return path

def bfs(target, path):
    result = set()
    q = deque([(target, path[target])])
    while q:
        now, prev_list = q.popleft()
        for prev_node in prev_list:
            if (prev_node, now) in result:
                continue
            result.add((prev_node, now))
            q.append((prev_node, path[prev_node]))
    
    return result

def almost_dijkstra(N, graph, start, edges):
    dist = [maxsize] * (N+1)
    dist[start] = 0

    q = [(0, start)]
    while q:
        acc_dist, stopover = heappop(q)
        for next_node, plus_dist in graph[stopover]:
            if (stopover, next_node) in edges:
                continue
            new_dist = acc_dist + plus_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(q, (new_dist, next_node))
    
    return dist

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    
    S, D = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U].append((V, P))

    path = dijkstra(N, graph, S)
    edges = bfs(D, path)
    dist = almost_dijkstra(N, graph, S, edges)

    print(dist[D] if dist[D] < maxsize else -1)

'''
6 8
0 5
0 1 1
1 2 1
2 3 1
3 4 1
4 5 1
0 2 2
2 5 10
0 5 5
'''