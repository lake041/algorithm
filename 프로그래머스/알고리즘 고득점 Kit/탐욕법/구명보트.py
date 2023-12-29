# 자주하는 실수
# 최대 2명씩... 어쩐지 너무 어렵더라...
# 문제를 천천히 똑바로 읽자

from collections import deque

def solution(people, limit):
    people.sort(reverse = True)
    q = deque(people)
    
    cnt = 0
    while True:
        if len(q) <= 1:
            cnt += 1 if len(q) else 0
            break 
        
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
        else:
            q.popleft()
            
        cnt += 1
    
    return cnt
