def solution(cap, n, deliveries, pickups):
    D = [index+1 for index, num in enumerate(deliveries) for _ in range(num)]
    P = [index+1 for index, num in enumerate(pickups) for _ in range(num)]
        
    dist = 0
    while D or P:
        farthest = max((D[-1] if D else 0), (P[-1] if P else 0))
        dist += farthest * 2
        for _ in range(cap):
            if D: D.pop()
            if P: P.pop()
        
    return dist