from sys import maxsize, stdin
from heapq import heappop, heappush
input = stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, target = map(int, input().split())

dist = [maxsize] * (N+1)
path = [[] for _ in range(N+1)]
dist[start] = 0
path[start].append(start)

q = [(0, start, [start])]
while q:
    acc_dist, stopover, acc_path = heappop(q)
    if acc_dist > dist[stopover]:
        continue

    for next_node, plus_dist in graph[stopover]:
        new_dist = acc_dist + plus_dist
        new_path = acc_path + [next_node]
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            path[next_node] = new_path
            heappush(q, (new_dist, next_node, new_path))

print(dist[target])
print(len(path[target]))
print(*path[target])