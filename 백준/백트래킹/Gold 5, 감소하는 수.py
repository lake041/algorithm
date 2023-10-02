from sys import stdin
from itertools import combinations
input = stdin.readline
N = int(input())
nums = [9-i for i in range(0, 10)]

ans = [0]
cnt = 0
for i in range(1, 11):
    combi = combinations(nums, i)
    for x in combi:
        if x[0] != 0:
            ans.append(int(''.join(map(str, list(x)))))
            cnt += 1
            continue
    if cnt >= N:
        break
ans.sort()

if N <= len(ans)-1:
    print(ans[N])
else:
    print(-1)