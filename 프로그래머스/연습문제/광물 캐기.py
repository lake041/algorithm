from collections import deque, Counter

MAP = {
    "diamond": {0:1, 1:5, 2:25},    
    "iron": {0:1, 1:1, 2:5},    
    "stone": {0:1, 1:1, 2:1},    
}

def cal(group, pick):
    group = group[:-1]

    fatigue = 0    
    for mineral in group:
        fatigue += MAP[mineral][pick]
    
    return fatigue

def solution(picks, minerals):
    minerals = deque(minerals)
    N = len(minerals)
    G = min(sum(picks), N//5 if N%5==0 else N//5+1)
    picks = [index for index, num in enumerate(picks) for _ in range(num)]
    
    groups = []
    
    for _ in range(G):
        group = [minerals.popleft() for _ in range(min(5, len(minerals)))]
        c = Counter(group)
        score = c["diamond"]*25 + c["iron"]*5 + c["stone"]
        group.append(score)
        groups.append(group)
    
    groups.sort(key = lambda x: (-x[-1], len(x)))

    fatigue = sum([cal(group, pick) for group, pick in zip(groups, picks)])
    
    return fatigue