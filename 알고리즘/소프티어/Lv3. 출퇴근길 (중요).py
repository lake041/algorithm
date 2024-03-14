from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start, graph, visited):
    q = deque([start])
    visited[start]=1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next]:
                continue
            visited[next] = 1
            q.append(next)

n, m = map(int,input().split())

graph = [[]for _ in range(n+1)]
graph_re = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph_re[b].append(a)
S, T = map(int, input().split())

fromS=[False]*(n+1)
fromS[T] = True
bfs(S, graph, fromS)

fromT=[False]*(n+1)
fromT[S] = True
bfs(T, graph, fromT)

toS=[False]*(n+1)
bfs(S, graph_re, toS)

toT=[False]*(n+1)
bfs(T, graph_re, toT)

ans = sum(1 for i in range(1, n+1) if fromS[i] and fromT[i] and toS[i] and toT[i]) - 2
print(ans)