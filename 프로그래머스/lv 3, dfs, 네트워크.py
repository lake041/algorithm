from collections import deque

def solution(N, computers):
    visited = [False]*N
    answer = 0
    
    def dfs(graph, start):
        nonlocal N
        q = deque([start])
        while q:
            now = q.popleft()
            if visited[now] == False:
                visited[now] = True
                q.extend([i for i in range(N) if graph[now][i] == 1])

    for start in range(N):
        if visited[start] == False:
            dfs(computers, start)
            answer += 1
    
    return answer