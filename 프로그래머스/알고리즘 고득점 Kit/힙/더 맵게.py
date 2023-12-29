from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while True:        
        first = heappop(scoville)
        if first >= K:
            break
            
        if not scoville:
            cnt = -1
            break

        second = heappop(scoville)
        heappush(scoville, first+second*2)
        cnt += 1

    return cnt