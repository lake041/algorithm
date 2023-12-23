from collections import deque

T = [deque(list(input())) for _ in range(4)]
K = int(input())
orders = [(int(x)-1, int(y)) for x, y in [input().split() for _ in range(K)]]

for i, d in orders:
    target = {i:d}
    for index in range(i+1, 4):
        if index-1 in target and T[index-1][2] != T[index][6]:
            target[index] = -target[index-1]
    for index in range(i-1, -1, -1):
        if index+1 in target and T[index+1][6] != T[index][2]:
            target[index] = -target[index+1]

    for index, direction in target.items():
        T[index].rotate(direction)

print(sum([2**index for index, value in enumerate(T) if value[0]=="1"]))