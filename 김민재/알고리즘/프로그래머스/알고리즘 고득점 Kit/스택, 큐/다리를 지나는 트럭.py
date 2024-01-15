from collections import deque

def solution(bridge_length, weight, truck):
    bridge = deque([0]*bridge_length)
    truck = deque(truck)
    total = 0
    time = 0
    
    # debug = []
    
    while True:
        if not truck and not total:
            break

        out = bridge.popleft()
        total -= out
        # debug.append(out)

        if truck and total + truck[0] <= weight:    
            next = truck.popleft()
            total += next
            bridge.append(next)
        else:
            bridge.append(0)
        
        time += 1

    return time