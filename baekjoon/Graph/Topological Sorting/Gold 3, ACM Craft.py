from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input())



