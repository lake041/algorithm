from sys import maxsize
from collections import deque, defaultdict
N, K = map(int, input().split())

'''
걷기 X-1, X+1
순간이동 2*X
K, K+1, K+1+2, K+1+2+3

2x -> 
x+1 
x-1 
'''

def k_val(cnt):
    return K + cnt*(cnt+1)//2

def is_even(x):
    return True if x%2==0 else False


v_even = defaultdict(bool)
v_odd = defaultdict(bool)

q = deque([(N, 0)])
ans = -1
while q:
    now, cnt = q.popleft()
    if now==k_val(cnt):
        ans = cnt
        break

    if 0<=now*2<=500_000:
        q.append((now*2, cnt+1))
    if 0<=now+1<=500_000:
        q.append((now+1, cnt+1))
    if 0<=now-1<=500_000:
        q.append((now-1, cnt+1))

print(ans)