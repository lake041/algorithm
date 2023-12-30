from collections import deque

def solution(bridge_length, weight, truck):
    bridge = deque([0]*bridge_length)
    truck = deque(truck)
    total_weight = 0
    time = 0
    
    while truck or total_weight:
        total_weight -= bridge.popleft()

        if truck and total_weight + truck[0] <= weight:    
            next = truck.popleft()
            total_weight += next
            bridge.append(next)
        else:
            bridge.append(0)
        
        time += 1

    return time