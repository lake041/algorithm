from collections import deque

def solution(x, y, n):
    answer = -1
    
    q = deque([(x, 0)])
    visited = set([x])
    while q:
        now, cnt = q.popleft()
        if now == y:
            answer = cnt
            break
        for next in [now*2, now*3, now+n]:
            if next <= y and next not in visited:
                visited.add(next)
                q.append((next, cnt+1))
    
    return answer