from collections import deque

picks = [1, 3, 2]
picks = ['diamond']*picks[0] + ['iron']*picks[1] + ['stone']*picks[2]
picks = deque(picks)

print(picks)