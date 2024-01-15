from collections import deque

S = int(input())

q = deque([(1, 0, 0)])
visited = set((1, 0, 0))

while q:
    screen, clip, cnt = q.popleft()

    if screen == S:
        print(cnt)
        break

    for screen, clip in [(screen+clip, clip), (screen, screen), (screen-1, clip)]:
        if (screen, clip) not in visited:
            q.append((screen, clip, cnt+1))
            visited.add((screen, clip))
