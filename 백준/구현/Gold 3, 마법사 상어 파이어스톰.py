# https://www.acmicpc.net/problem/20058

from itertools import product
from collections import deque
from sys import stdin
input = stdin.readline

N, Q = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(2**N)]
orders = list(map(int, input().split()))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def rotate(order):
    size = 2**order
    temp = [[0]*len(bod) for _ in range(len(bod))]
    for ny, nx in product(range(0, len(bod), size), repeat=2):
        for dy, dx in product(range(size), repeat=2):
            temp[ny+dx][nx+size-dy-1] = bod[ny+dy][nx+dx]
        for dy, dx in product(range(size), repeat=2):
            bod[ny+dy][nx+dx] = temp[ny+dy][nx+dx]

def melt():
    melt_list = []
    for ny, nx in product(range(len(bod)), repeat=2):
        count = 0
        for u, v in zip(dy, dx):
            py, px = ny+u, nx+v
            if 0<=py<len(bod) and 0<=px<len(bod) and bod[py][px]>=1:
                count += 1
        if count < 3 and bod[ny][nx]>=1:
            melt_list.append((ny, nx))
    
    for (y, x) in melt_list:
        bod[y][x] -= 1

def find_answer1():
    answer1 = 0
    for ny, nx in product(range(len(bod)), repeat=2):
        answer1 += bod[ny][nx]
    return answer1

def find_answer2():
    answer2 = 0
    check = [[False]*len(bod) for _ in range(len(bod))]
    for ny, nx in product(range(len(bod)), repeat=2):
        if bod[ny][nx]==0 or check[ny][nx]==True:
            continue
        q = deque()
        q.append((ny, nx))
        check[ny][nx] = True
        count = 1
        while q:
            y, x = q.popleft()
            for u, v in zip(dy, dx):
                py, px = y+u, x+v
                if 0<=py<len(bod) and 0<=px<len(bod) and bod[py][px]>=1 and check[py][px]==False:
                    q.append((py, px))
                    check[py][px] = True
                    count += 1
        answer2 = max(answer2, count)
    return answer2

for order in orders:
    rotate(order)
    melt()
print(find_answer1())
print(find_answer2())

# for row in bod:
#     print(row)

'''
49
(4, 0)
(4+0, 0+1) <- (4+2, 0+0)

3 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 2 3 4 0 0 0 0
5 6 7 8 0 0 0 0
4 3 2 1 0 0 0 0
8 7 6 5 0 0 0 0
1
'''

# print('original')
# for row in bod:
#     print(row)
# print()

# print('rotated')
# melt()
# for row in bod:
#     print(row)
# print()