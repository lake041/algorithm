from collections import deque

def solution(q1, q2):
    q1, q2 = deque(q1), deque(q2)
    
    half = ( sum(q1) + sum(q2) ) / 2
    now = sum(q1)
    cnt = 0
    while True:
        if cnt > 700_000:
            return -1
        
        if now == half:
            return cnt

        if now > half:
            x = q1.popleft()
            q2.append(x)
            now -= x
            cnt += 1
        
        elif now < half:
            x = q2.popleft()
            q1.append(x)
            now += x
            cnt += 1