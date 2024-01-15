from collections import deque

def solution(N, results):
    W = [set() for _ in range(N)]
    L = [set() for _ in range(N)]
    for a, b in results:
        a, b = a-1, b-1
        W[a].add(b)
        L[b].add(a)

    for i in range(N):
        q = deque([i])
        visited = [False]*N
        visited[i] = True
        while q:
            now = q.popleft()
            for can_win in W[now]:
                if visited[can_win]:
                    continue
                q.append(can_win)
                W[i].add(can_win)
                visited[can_win] = True

        q = deque([i])
        visited = [False]*N
        visited[i] = True
        while q:
            now = q.popleft()
            for cant_win in L[now]:
                if visited[cant_win]:
                    continue
                q.append(cant_win)
                L[i].add(cant_win)
                visited[cant_win] = True
            
            
    return sum([1 if len(L[i])+len(W[i])==N-1 else 0 for i in range(N)])