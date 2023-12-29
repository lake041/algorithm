# 복습 필요

from heapq import heappush, heappop

def solution(operations):
    maxq, minq = [], []
    deleted_index = []

    for i in range(len(operations)):
        op, num = operations[i].split()
        num = int(num)
        if op=="I":
            heappush(maxq, (-num, i))
            heappush(minq, (num, i))
        elif num == 1:
            if maxq:
                _, index = heappop(maxq)
                deleted_index.append(index)
        elif num == -1:
            if minq:
                _, index = heappop(minq)
                deleted_index.append(index)

        while minq and minq[0][1] in deleted_index:
            heappop(minq)
        while maxq and maxq[0][1] in deleted_index:
            heappop(maxq)
                
    return [-heappop(maxq)[0], heappop(minq)[0]] if maxq else [0, 0]