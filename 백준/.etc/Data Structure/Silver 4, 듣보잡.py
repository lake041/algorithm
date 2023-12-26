from collections import defaultdict
from sys import stdin
input = stdin.readline

N,M = map(int, input().split())
d = defaultdict(int)

for _ in range(N):
    d[input().rstrip()] += 1
for _ in range(M):
    d[input().rstrip()] += 1
    
x = []
for key in d:
    if d[key] == 2:
        x.append(key)

x.sort()
print(len(x))
for item in x:
    print(item)