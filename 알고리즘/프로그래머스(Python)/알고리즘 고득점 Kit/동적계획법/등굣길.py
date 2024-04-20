from itertools import product

def solution(C, R, puddles):
    puddles = set((y-1, x-1) for x, y in puddles)

    val = [0] * C
    for x in range(C):
        if (0, x) in puddles:
            break
        val[x] = 1
    
    for row, col in product(range(1, R), range(C)):
        if (row, col) in puddles:
            val[col] = 0
        elif col > 0:
            val[col] = (val[col] + val[col-1]) % 1_000_000_007
            
    return val[-1]
