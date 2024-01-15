# https://www.acmicpc.net/problem/11725
# 재귀도 연습해야 되는데

from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
depth = [0]*(N+1)
depth[1] = 0
visited[1] = True
q = deque()
q.append(1)
while q:
    for _ in range(len(q)):
        parent = q.popleft()
        d = depth[parent]
        for x in graph[parent]:
            if visited[x] == True:
                continue
            visited[x] = True
            depth[x] = d+1
            q.append(x)

for child in range(2, N+1):
    for parent in graph[child]:
        if depth[parent] == depth[child] - 1:
            print(parent)
            break