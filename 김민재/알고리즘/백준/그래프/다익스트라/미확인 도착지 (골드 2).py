from sys import maxsize, stdin
from heapq import heappop, heappush
input = stdin.readline

def dijkstra(graph, start, N):
    dist = [maxsize] * (N+1)
    dist[start] = 0

    q = [(0, start)]
    while q:
        acc_dist, stopover = heappop(q)
        if acc_dist > dist[stopover]:
            continue

        for next_node, plus_dist in graph[stopover]:
            new_dist = acc_dist + plus_dist
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heappush(q, (new_dist, next_node))

    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    start, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    dist_gh = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a, b) in [(g, h), (h, g)]:
            dist_gh = d

    targets = [int(input()) for _ in range(t)]
    
    dist_s = dijkstra(graph, start, n)
    dist_g = dijkstra(graph, g, n)
    dist_h = dijkstra(graph, h, n)
    
    possible = []
    for target in targets:
        if dist_s[target] == dist_g[start] + dist_gh + dist_h[target] or \
            dist_s[target] == dist_h[start] + dist_gh + dist_g[target]:
            possible.append(target)
    possible.sort()

    print(*possible)



'''
1
6 9 2
2 3 1
1 2 1
1 3 3
2 4 4
2 5 5
3 4 3
3 6 2
4 5 4
4 6 3
5 6 7
5
6

2 3 1
3 6 2

2 4 4
4 6 3
'''