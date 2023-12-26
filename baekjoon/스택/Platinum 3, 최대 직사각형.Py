from sys import stdin
input = stdin.readline

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break

    bod = [list(map(int, input().split())) + [0] for _ in range(N)]
    H = [0]*(M+1)
    nemo = []

    for row in bod:
        H = [prev+1 if now else 0 for prev, now in zip(H, row)]
        stack = [(-1, 0)]
        for index, height in enumerate(H):
            while stack and height < stack[-1][1]:
                h = stack.pop()[1]
                w = index - stack[-1][0] - 1
                nemo.append(h*w)
            stack.append((index, height))
    
    print(max(nemo) if nemo else 0)