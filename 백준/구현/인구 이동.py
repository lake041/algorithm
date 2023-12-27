from collections import defaultdict, deque
from itertools import product

N, L, R = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(sy, sx, group, visited, group_index):
    q = deque([(sy, sx)])
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and L<=abs(bod[y][x]-bod[ny][nx])<=R:
                q.append((ny, nx))
                visited[ny][nx] = True
                group[y][x] = group_index
                group[ny][nx] = group_index

day = 0
while True:
    group = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    group_index = 1
    for y, x in product(range(N), range(N)):
        if visited[y][x]:
            continue
        bfs(y, x, group, visited, group_index)
        if group[y][x]:
            group_index = group[y][x] + 1

    visited = [[False]*N for _ in range(N)]
    group_members = defaultdict(list)
    
    for y, x in product(range(N), range(N)):
        if not group[y][x]:
            continue
        group_index = group[y][x]
        group_members[group_index].append((y, x))
    
    done = True

    for members in group_members.values():
        result = sum([bod[y][x] for y, x in members]) // len(members)
        if any(bod[y][x] != result for y, x in members):
            done = False
        for y, x in members:
            bod[y][x] = result

    if done:
        break
    day += 1
    print(group_members)
    for row in bod:
        print(row)

print(day)

'''
9 1 2
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
3 4 5 6 7 8 9 1 2
2 3 4 1 2 3 4 5 6
3 4 5 8 9 1 2 3 4
5 5 5 5 5 1 2 4 4
1 1 1 1 2 3 4 5 6
9 8 7 6 5 4 3 3 3
2 3 4 1 2 3 4 5 6

3 1 2
1 2 3
6 5 4
7 8 9

3 1 2
1 8 7
2 9 6
3 0 5

3 1 2
2 4 7
12 0 8
15 16 18
'''