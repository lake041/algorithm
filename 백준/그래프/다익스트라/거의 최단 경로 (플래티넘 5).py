from sys import maxsize, stdin
from collections import deque
from heapq import heappop, heappush
input = stdin.readline

def dijkstra(N, graph, start):
    dist = [maxsize] * (N+1)
    dist[start] = 0
    prev = [[] for _ in range(N+1)]

    q = [(0, start)]
    while q:
        acc_dist, stopover = heappop(q)
        if acc_dist < dist[stopover]:
            continue
        for next_node, plus_dist in graph[stopover]:
            new_dist = acc_dist + plus_dist
            if new_dist == dist[next_node]:
                prev[next_node].append(stopover)
            elif new_dist < dist[next_node]:
                dist[next_node] = new_dist
                prev[next_node] = [stopover]
                heappush(q, (new_dist, next_node))

    return prev

def almost_dijkstra(N, graph, start, target, edges):
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
    
    return dist[target] if dist[target] < maxsize else -1

def bfs(target, prev):
    result = set()
    q = deque([(target, prev[target])])
    while q:
        now, prev_list = q.popleft()
        for prev_node in prev_list:
            result.add((prev_node, now))
            q.append((prev_node, prev[prev_node]))
    
    return result


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
    ans = almost_dijkstra(N, graph, S, D, edges)

    print(ans)


'''
7 9
0 6
0 1 1
0 2 1
0 3 2
0 4 3
1 5 2
2 6 4
3 6 2
4 6 4
5 6 1

4 6
0 2
0 1 1
1 2 1
1 3 1
3 2 1
2 0 3
3 0 2

6 8
0 1
0 1 1
0 2 2
0 3 3
2 5 3
3 4 2
4 1 1
5 1 1
3 0 1

4 5
0 2
0 1 1
0 3 5
1 2 2
1 3 1
3 2 1

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

4 5
0 2
0 1 1
0 3 5
1 2 2
1 3 1
3 2 1

0 0
'''