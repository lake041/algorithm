from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    jobs.sort()
    jobs = deque(jobs)
    L = len(jobs)
    q = []
    memo = []
    
    time = 0
    while True:
        if not jobs and not q:
            break
        
        while True:
            if jobs and jobs[0][0] <= time:
                request_time, duration = jobs.popleft()
                heappush(q, [duration, request_time])
            else:
                break
                
        if not q:
            time = jobs[0][0]
            continue
        
        duration, request_time = heappop(q)
        time += duration
        memo.append(time - request_time)
    
    return sum(memo)//L