from collections import deque
from math import ceil


def solution(picks, minerals):
    answer = 0
    pick_list = deque(['diamond']*picks[0] + ['iron']*picks[1] + ['stone']*picks[2])
    minerals = deque(minerals)

    next_list = []    
    score = {'diamond':25, 'iron':5, 'stone':1}
    for _ in range(min(len(pick_list), ceil(len(minerals)/5))):
        next = []
        num = 0
        hap = 0
        while minerals and num < 5:
            mineral = minerals.popleft()
            next.append(mineral)
            hap += score[mineral]
            num += 1
        next.append(hap)
        next_list.append(next)
    next_list.sort(key = lambda x: -x[-1])
    next_list = deque(next_list)
    
    fatigue = {
        'diamond': {'diamond':1, 'iron':1, 'stone':1},
        'iron': {'diamond':5, 'iron':1, 'stone':1},
        'stone': {'diamond':25, 'iron':5, 'stone':1},
    }
    
    while next_list and pick_list:
        pick = pick_list.popleft()
        next = next_list.popleft()
        for mineral in next:
            answer += fatigue[pick].get(mineral,0)
                    
    return answer