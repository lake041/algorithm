# https://www.acmicpc.net/problem/6549

from sys import stdin
input = stdin.readline

while True:
    heights = list(map(int, input().split()))[1:]
    if not heights:
        break

    heights += [0]
    stack = [(-1, 0)]
    nemo = []

    for index, height in enumerate(heights):
        while stack and height < stack[-1][1]:
            h = stack.pop()[1]
            w = index - stack[-1][0] - 1
            nemo.append(h*w)
        stack.append((index, height))
    
    print(max(nemo) if nemo else 0)