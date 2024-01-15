from collections import defaultdict
from itertools import permutations

def solution(friends, gifts):
    score = {name: 0 for name in friends}
    record = defaultdict(int)
    next_month = {name: 0 for name in friends}

    for giver, taker in [gift.split() for gift in gifts]:
        score[giver] += 1
        score[taker] -= 1
        record[(giver, taker)] += 1
    
    for giver, taker in permutations(friends, 2):
        if record[(giver, taker)] < record[(taker, giver)]:
            next_month[taker] += 1
        if record[(giver, taker)] == record and [(taker, giver)] and score[giver] < score[taker]:
            next_month[taker] += 1
                
    return max(next_month.values())