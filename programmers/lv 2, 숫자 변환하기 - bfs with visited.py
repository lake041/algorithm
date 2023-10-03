from collections import deque

def solution(x, y, n):
    answer = -1
    q = deque([(x, 0)])
    while q:
        now, cnt = q.popleft()
        if now == y:
            answer = cnt
            break
        if now > y:
            continue
        q.append((now*2, cnt+1))
        q.append((now*3, cnt+1))
        q.append((now+n, cnt+1))
    
    return answer