from collections import defaultdict, deque

# 반례/디버깅 지옥...
# 애초에 로직 짜는 지능이 부족해...

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(arrows):
    visited = defaultdict(bool)
    segments = set()
    py, px, y, x = 0, 0, 0, 0
    for arrow in arrows:
        py, px, y, x = y, x, y+dy[arrow], x+dx[arrow]
        segments.add((py, px, y, x))
        segments.add((y, x, py, px))
    
    q = deque([(0, 0)])
    visited[(0, 0)] = True
    visited_segments = set()
    cnt = 0
    debug = []
    while q:
        y, x = q.popleft()
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            my, mx = (y+ny)/2, (x+nx)/2
            if (y, x, ny, nx) in segments:
                debug.append((y, x, ny, nx, my, mx, visited[(my, mx)]))
                if visited[(ny, nx)] and (y, x, ny, nx) not in visited_segments:
                    visited_segments.add((y, x, ny, nx))
                    visited_segments.add((ny, nx, y, x))
                    cnt += 1
                    if visited[(my, mx)]:
                        cnt += 1
                    visited[(my, mx)] = True
                elif visited[(ny, nx)] and (y, x, ny, nx) in visited_segments:
                    continue
                else:
                    q.append((ny, nx))
                    visited[(ny, nx)] = True
                    visited_segments.add((y, x, ny, nx))
                    visited_segments.add((ny, nx, y, x))
                    if visited[(my, mx)]:
                        cnt += 1
                    visited[(my, mx)] = True
                    
    return cnt