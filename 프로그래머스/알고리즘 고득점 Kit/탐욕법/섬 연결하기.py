# 자주하는 실수
# 한 줄씩 천천히 읽어보자

from collections import deque

def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    graph = [[] for _ in range(n)]
    
    def connected(a, b):
        q = deque([a])
        visited = [False]*n
        visited[a] = True

        while q:
            now = q.popleft()
            if now == b:
                return True
            
            for next in graph[now]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True

        return False
        
    total_cost = 0
    cnt = 0
    
    for a, b, cost in costs:
        if not connected(a, b):
            graph[a].append(b)
            graph[b].append(a)
            total_cost += cost
            cnt += 1
        
        if cnt == n-1:
            break
    
    return total_cost