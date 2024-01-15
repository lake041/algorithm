# https://www.acmicpc.net/problem/14891

from collections import deque
from sys import stdin
input = stdin.readline

gear = [deque(map(int, list(input().rstrip()))) for _ in range(4)]
K = int(input())
orders = [list(map(int, input().split())) for _ in range(K)]
# 2: 3시, 6: 9시

def rotate(num, direction):
    if direction == 1:
        gear[num].appendleft(gear[num].pop())
    if direction == -1:
        gear[num].append(gear[num].popleft())

for order in orders:
    num, direction = order
    num -= 1

    target = {}
    for i in range(3):
        if gear[i][2] != gear[i+1][6]:
            target[(i, i+1)] = True
        else:
            target[(i, i+1)] = False

    rotate(num, direction)

    next_direction = direction
    for i in range(num, 3, 1):
        if target[(i, i+1)]:
            next_direction *= -1
            rotate(i+1, next_direction)
        else:
            break

    next_direction = direction
    for i in range(num, 0, -1):
        if target[(i-1, i)]:
            next_direction *= -1
            rotate(i-1, next_direction)
        else:
            break

print(sum([gear[i][0]*(2**i) for i in range(4)]))


'''
11111110
00000000
11111111
11111111
1
2 -1

12

10001011
10000011
01011011
00111101
5
1 1
2 1
3 1
4 1
1 -1

6
'''