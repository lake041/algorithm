from math import inf
from itertools import product
from sys import stdin
input = stdin.readline

bod = [list(input().rstrip()) for _ in range(10)]
# print(list(map(list, product(range(2), repeat=10))))

def switch(x):
    return 'O' if x =='#' else '#'

def turn(row, order):
    di = [-1, 0, 1]
    for i, di in product(range(10), di):
        if order[i]==1 and 0<=i+di<10:
            row[i+di] = switch(row[i+di])
    return row

def prev_turn(row, order):
    for i in range(10):
        if order[i]==1:
            row[i] = switch(row[i])
    return row

def next_order(row):
    order = [0]*10
    for index, status in enumerate(row):
        if status == "O":
            order[index] = 1
    return order

answer = inf
orders = list(map(list, product(range(2), repeat=10)))
x = 1
for init_order in orders:
    now = bod[0][:]
    now = turn(now, init_order)
    count = sum(init_order)

    # 이전 row에서 수행했던 order
    prev_order = init_order
    # 다음 row에서 #####으로 만들기 위한 order
    order = next_order(now)
    
    for i in range(1, 10):
        now = bod[i][:]
        # 일단 이전 row에서 수행했던 order
        now = prev_turn(now, prev_order)
        now = turn(now, order)
        count += sum(order)

        prev_order = order
        order = next_order(now)

    if now == ['#']*10:
        answer = min(answer, count)
print(-1 if answer==inf else answer)

# x = ['#', 'O', '#', '#', '#', '#', '#', '#', '#', '#']
# o = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# x = turn(x, o)
# print(x)

'''
[1, 0, 1, 0, 0, 0, 0, 1, 0, 1]

O########O
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
#OOOOOOOO#
O########O

100
'''