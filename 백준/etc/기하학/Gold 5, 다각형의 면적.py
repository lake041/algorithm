from collections import deque
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(100_000)

def heron(vertex1, vertex2, vertex3):
    y1, x1 = vertex1
    y2, x2 = vertex2
    y3, x3 = vertex3

    a = ((y1-y2)**2 + (x1-x2)**2)**0.5
    b = ((y2-y3)**2 + (x2-x3)**2)**0.5
    c = ((y3-y1)**2 + (x3-x1)**2)**0.5
    s = (a + b + c)/2

    return (s*(s-a)*(s-b)*(s-c))**0.5

def polygon(vertex_list):
    if len(vertex_list) < 3:
        return

    global area
    area += heron(vertex_list[0], vertex_list[1], vertex_list[2])
    vertex_list.popleft()
    polygon(vertex_list)

N = int(input())
vertex_list = []
for _ in range(N):
    y, x = map(int, input().split())
    vertex_list.append((y, x))
vertex_list.sort()
vertex_list = deque(vertex_list)

area = 0
polygon(vertex_list)
print(area)