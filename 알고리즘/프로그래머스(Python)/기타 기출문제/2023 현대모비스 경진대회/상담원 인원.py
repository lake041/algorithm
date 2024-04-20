from collections import deque
from itertools import product
from copy import deepcopy

# rq의 멘토가 x명일 때 기다리는 시간
def waiting_time(x, rq_input):
    cq = deque()
    wq = deque()
    rq = deepcopy(rq_input)

    now = 0
    total = 0
    while rq or wq:
        temp = deque()
        for end_time in cq:
            if end_time != now:
                temp.append(end_time)
        cq = temp
        while rq and rq[0][0] == now:
            wq.append(rq.popleft()[1])
        while wq and len(cq) < x:
            need = wq.popleft()
            cq.append(now+need)
        now += 1
        total += len(wq)
    
    return total
    

def solution(K, N, reqs):
    rqs = [deque() for _ in range(K)]
    for a, b, c in reqs:
        c -= 1
        rqs[c].append([a, b])

    # memo[A][B] 멘토가 A명일 때 B번 유형의 waiting time 총합
    wt_memo = [[0]*K for _ in range(N+1)]
    for A, B in product(range(1, N+1), range(K)):
        wt_memo[A][B] = waiting_time(A, rqs[B])
    
    ag_memo = {K:[1]*K}
    for i in range(K+1, N+1):
        prev = ag_memo[i-1]
        diff = [wt_memo[prev[i]][i]-wt_memo[prev[i]+1][i] for i in range(K)]
        plus = diff.index(max(diff))
        ag_memo[i] = [num if index!=plus else num+1 for index, num in enumerate(prev)]

    op = [x for x in ag_memo[N]]
    answer = sum([wt_memo[op[i]][i] for i in range(K)])
    return answer