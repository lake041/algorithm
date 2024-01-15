# 복습 필수

from sys import maxsize
from heapq import heappush, heappop

def solution(a, c, problems):
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    problems.sort()
    
    at = max([x[0] for x in problems])
    ct = max([x[1] for x in problems])
    cost_max = (at-a) + (ct-c)
    
    pq = []
    # cost[i][j]: 알고력 i, 코딩력j까지 도달하는 최단 시간
    cost = [[maxsize]*(ct+1) for _ in range(at+1)]

    a = min(a, at)
    c = min(c, ct)
    heappush(pq, (0, a, c))
    cost[a][c] = 0
    
    while pq:
        cost_now, a_now, c_now = heappop(pq)
        if cost_now > cost[a_now][c_now]:
            continue
        
        next = []
        for a_req, c_req, a_rwd, c_rwd, cost_plus in problems:
            if a_now < a_req and c_now < c_req:
                break
            if a_now >= a_req and c_now >= c_req:
                next.append((cost_now+cost_plus, a_now+a_rwd, c_now+c_rwd))
        
        for cost_next, a_next, c_next in next:
            a_next = min(at, a_next)
            c_next = min(ct, c_next)
            if cost_next < cost[a_next][c_next]:
                cost[a_next][c_next] = cost_next
                heappush(pq, (cost_next, a_next, c_next))
                
    return cost[at][ct]