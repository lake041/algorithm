from sys import maxsize, stdin
from heapq import heappop, heappush
input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

def fox(start):
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

def wolf(start):
    dist = [[maxsize, maxsize] for _ in range(N+1)] 
    dist[start][1] = 0

    q = [(0, start, 1)]
    while q:
        acc_dist, stopover, flag = heappop(q)
        if acc_dist > dist[stopover][flag]:
            continue
        for next_node, plus_dist in graph[stopover]:
            plus_dist = plus_dist / 2 if flag else plus_dist * 2
            new_dist = acc_dist + plus_dist 
            if new_dist < dist[next_node][1 - flag]:
                dist[next_node][1 - flag] = new_dist
                heappush(q, (new_dist, next_node, 1 - flag))
    
    dist = [min(x) for x in dist]

    return dist

print(sum(f < w for f, w in zip(fox(1), wolf(1))))