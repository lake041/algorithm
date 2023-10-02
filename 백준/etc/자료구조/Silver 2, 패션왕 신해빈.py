'''
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
'''

from collections import defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    redis = defaultdict(int)
    for _ in range(N):
        name, type = input().split()
        redis[type] += 1
    ans = 1
    for key in redis:
        ans *= redis[key] + 1
    print(ans-1)