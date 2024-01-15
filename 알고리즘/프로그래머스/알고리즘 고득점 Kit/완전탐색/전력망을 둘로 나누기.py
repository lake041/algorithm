from collections import deque

def bfs(n, start, graph, edge):
    a, b = edge
    graph[a].remove(b)
    graph[b].remove(a)

    count = 1
    visited = [False] * (n+1)

    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                count += 1

    graph[a].append(b)
    graph[b].append(a)

    return count

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    return min(abs(n-bfs(n, n, graph, edge)*2) for edge in wires)