from itertools import product

R, C = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def watch1(y, x, d, s):
    ny, nx = y+dy[d], x+dx[d]
    while 0<=ny<R and 0<=nx<C and bod[ny][nx] != 6:
        if not bod[ny][nx]:
            s.add((ny, nx))
        ny, nx = ny+dy[d], nx+dx[d]

def watch2(y, x, d, s):
    watch1(y, x, d, s)
    watch1(y, x, (d+2)%4, s)

def watch3(y, x, d, s):
    watch1(y, x, d, s)
    watch1(y, x, (d+1)%4, s)

def watch4(y, x, d, s):
    watch1(y, x, d, s)
    watch1(y, x, (d+1)%4, s)
    watch1(y, x, (d+3)%4, s)

def watch5(y, x, d, s):
    watch1(y, x, d, s)
    watch1(y, x, (d+1)%4, s)
    watch1(y, x, (d+2)%4, s)
    watch1(y, x, (d+3)%4, s)

f = { 1:watch1, 2:watch2, 3:watch3, 4:watch4, 5:watch5 }

cameras = [(y, x) for y, x in product(range(R), range(C)) if bod[y][x] not in [0, 6]]
unwatched_num = sum([1 for y, x in product(range(R), range(C)) if not bod[y][x]])
results = []

for combi in product(range(4), repeat=len(cameras)):
    watched = set()
    for (y, x), d in zip(cameras, combi):
        camera_type = bod[y][x]
        f[camera_type](y, x, d, watched)
    results.append(unwatched_num - len(watched))

print(min(results))