from sys import maxsize
from collections import deque

N, K = map(int, input().split())

q = deque([(N, 0)])
memo = [maxsize] * 100_001
shortest_time = maxsize
shortest_cnt = 0

while q:
    cur, time = q.popleft()

    if time > shortest_time:
        continue

    if cur == K:
        if time < shortest_time:
            shortest_time = time
            shortest_cnt = 1
        elif time == shortest_time:
            shortest_cnt += 1
        continue
    
    if 0<=cur-1 and time+1 <= memo[cur-1]:
        q.append((cur-1, time+1))
        memo[cur-1] = time+1
    if cur+1<=100_000 and time+1 <= memo[cur+1]:
        q.append((cur+1, time+1))
        memo[cur+1] = time+1
    if cur*2<=100_000 and time+1 <= memo[cur*2]:
        q.append((cur*2, time+1))
        memo[cur*2] = time+1

print(shortest_time)
print(shortest_cnt)