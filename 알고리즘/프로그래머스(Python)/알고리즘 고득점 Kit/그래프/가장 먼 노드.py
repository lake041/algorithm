from sys import maxsize
from collections import deque

def solution(N, edge):
    graph = [[] for _ in range(N)]
    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        
    q = deque([(0, [], 0)])
    distance = [0] + [maxsize]*(N-1)
    
    while q:
        now, visited, cnt = q.popleft()
        for next in graph[now]:
            if next in visited:
                continue
            if distance[next] <= cnt+1:
                continue
            else:
                distance[next] = cnt+1
                q.append((next, [next]+visited, cnt+1))
    
    max_value = max(distance)
    
    return distance.count(max_value)