from sys import maxsize
from copy import deepcopy
from itertools import product

dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]

def rotate(bod, target, repeat):
    for y, x in target:
        bod[y][x] = (bod[y][x]+repeat)%4

def solution(bod):
    N = len(bod)
    ans = maxsize
    
    target = [[[] for x in range(N)] for y in range(N)]
    for y, x in product(range(N), range(N)):
        target[y][x] = [(ny, nx) for u, v in zip(dy, dx) if 0<=(ny:=y+u)<N and 0<=(nx:=x+v)<N]
    
    for combi in product(range(4), repeat=N):
        new = deepcopy(bod)
        sub = sum(combi)
        for index, repeat in enumerate(combi):
            rotate(new, target[0][index], repeat)
        
        for y, x in product(range(1, N), range(N)):
            repeat = (4-new[y-1][x]) % 4
            rotate(new, target[y][x], repeat)
            sub += repeat
        
        if max(max(row) for row in new) == 0:
            ans = min(ans, sub)

    return ans