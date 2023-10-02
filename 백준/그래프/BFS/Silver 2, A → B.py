# https://www.acmicpc.net/problem/16953

from collections import deque

A, B = map(int, input().split())
exist = False

q = deque([(A, 0)])
while q:
    num, cnt = q.popleft()
    if num == B:
        exist = True
        print(cnt+1)
        break

    if num*2 <= B:
        q.append((num*2, cnt+1))
    if num*10 + 1 <= B:
        q.append((num*10 + 1, cnt+1))

if not exist:
    print(-1)