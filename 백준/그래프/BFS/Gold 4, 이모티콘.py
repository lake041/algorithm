from collections import deque, defaultdict

S = int(input())

check = defaultdict(bool)
q = deque([(1, 0, 0)])
ans = 0
while q:
    now, clip, cnt = q.popleft()
    if check[(now, clip)]:
        continue
    if now == S:
        ans = cnt
        break
    check[(now, clip)] = True
    q.append((now, now, cnt+1))
    q.append((now+clip, clip, cnt+1))
    q.append((now-1, clip, cnt+1))
print(ans)
# x2, copy, delete