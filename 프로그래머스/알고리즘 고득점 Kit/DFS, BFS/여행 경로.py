from collections import deque

def solution(tickets):
    answer = ["ZZZ"]
    
    q = deque()
    q.append(["ICN", ["ICN"], []])
    while q:
        now, routes, visited = q.popleft()
        if len(routes) == len(tickets) + 1:
            answer = min(answer, routes)
            continue

        for i in range(len(tickets)):
            if i in visited:
                continue
            start, dest = tickets[i]
            if now == start:
                q.append([dest, routes+[dest], visited+[i]])
    
    return answer