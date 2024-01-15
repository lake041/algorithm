from collections import deque

def solution(cap, n, deliveries, pickups):
    D, P = [], []
    for i, num in enumerate(deliveries):
        D.extend([i+1]*num)
    for i, num in enumerate(pickups):
        P.extend([i+1]*num)

    ans = 0
    while True:
        if not D and not P:
            break
        if not P:
            last = D[-1]
            ans += last*2
            for _ in range(cap):
                if D:
                    D.pop()
        elif not D:
            last = P[-1]
            ans += last*2
            for _ in range(cap):
                if P:
                    P.pop()
        else:
            last = max(P[-1], D[-1])
            ans += last*2
            for _ in range(cap):
                if D:
                    D.pop()
                if P:
                    P.pop()

    return ans