from collections import defaultdict
from itertools import combinations
from sys import stdin
input = stdin.readline

N = int(input())
segment = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    segment.append([(y1, x1), (y2, x2)])

def judge(segment1, segment2):
    square = segment1 + segment2
    square.sort()
    if (square[0] in segment1) and (square[1] in segment2) and (square[2] in segment1) and (square[3] in segment2) :
        return True
    if (square[0] in segment2) and (square[1] in segment1) and (square[2] in segment2) and (square[3] in segment1) :
        return True
    return False

d = defaultdict(list)
for i, j in combinations(range(N), 2):
    if judge(segment[i], segment[j]):
        d[i].append(j)
        d[j].append(i)
print(d)

'''
- 2
- - -
3 - 3 - - -
- 2 - - -
'''