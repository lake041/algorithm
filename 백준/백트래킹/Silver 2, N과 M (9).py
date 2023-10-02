# 이런 걸 dfs로 풀 줄 알아야 하는데 무지성 itertools만 남용하네

from itertools import permutations
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

d = {}
for x in permutations(nums, M):
    if x not in d:
        d[x] = True
        print(*x)
    else:
        continue