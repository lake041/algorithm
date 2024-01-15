from sys import maxsize
from itertools import product

# 무지성 플로이드-워셜 실패
# 이건 대체 왜 쓰는 걸까?

def solution(N, edge):
    graph = [[maxsize]*N for _ in range(N)]
    for a, b in edge:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1
    
    for i in range(N):
        graph[i][i] = 0

    for k, i, j in product(range(N), range(N), range(N)):
        if graph[i][k] + graph[k][j] < graph[i][j]:
            graph[i][j] = graph[i][k] + graph[k][j]
    
    for i, j in product(range(N), range(N)):
        if graph[i][j] == maxsize:
            graph[i][j] = 0
    
    max_value = max(graph[0])
    count_max = graph[0].count(max_value)
    
    return count_max