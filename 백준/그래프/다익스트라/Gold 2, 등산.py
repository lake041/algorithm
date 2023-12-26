from heapq import heappush, heappop
from sys import stdin, maxsize
input = stdin.readline

N, M, D, E = map(int, input().split())
h = [0] + list(map(int, input().split()))
routes = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, n = map(int, input().split())
    routes[a].append((b, n))
    routes[b].append((a, n))

def dijkstra(graph, start):
    distance = [maxsize]*(N+1)
    distance[start] = 0
    q = []
    heappush(q, (distance[start], start))
    
    while q:
        cur_dist, cur_dest = heappop(q)
        if distance[cur_dest] < cur_dist:
            continue
        for new_dest, plus_dist in graph[cur_dest]:
            if h[cur_dest] >= h[new_dest]:
                continue
            new_dist = cur_dist + plus_dist
            if new_dist < distance[new_dest]:
                distance[new_dest] = new_dist
                heappush(q, (new_dist, new_dest))
    return distance

dist1 = dijkstra(routes, 1)
dist2 = dijkstra(routes, N)

ans = []
for i in range(2, N):
    if dist1[i]!=maxsize and dist2[i]!=maxsize:
        ans.append(h[i]*E-(dist1[i]+dist2[i])*D)
if not ans:
    print('Impossible')
else:
    print(max(ans))