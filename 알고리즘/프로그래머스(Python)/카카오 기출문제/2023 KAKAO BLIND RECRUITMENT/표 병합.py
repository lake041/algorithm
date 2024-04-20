from itertools import product

def solution(commands):
    bod = [[[] for _ in range(50)] for _ in range(50)]
    dic = {}
    
    for y, x in product(range(50), repeat=2):
        dic[(y, x)] = set([(y, x)])
    
    ans = []
    
    for command in commands:
        C = command.split()
        if C[0] == 'UPDATE' and len(C) == 4:
            r, c = map(lambda x: int(x)-1, (C[1], C[2]))
            value = C[3]
            hap = dic[(r, c)]
            for y, x in hap:
                bod[y][x] = value

        if C[0] == 'UPDATE' and len(C) == 3:
            value1, value2 = C[1], C[2]
            for y, x in product(range(50), repeat=2):
                bod[y][x] = value2 if bod[y][x] == value1 else bod[y][x]
        
        if C[0] == 'MERGE':
            r1, c1, r2, c2 = map(lambda x: int(x)-1, (C[1], C[2], C[3], C[4]))
            if bod[r1][c1]:
                value = bod[r1][c1]
            elif bod[r2][c2]:
                value = bod[r2][c2]
            else:
                value = []
                
            left, right = dic[(r1, c1)], dic[(r2, c2)]
            hap = left | right
            for y, x in hap:
                dic[(y, x)] = hap
                bod[y][x] = value 
        
        if C[0] == 'UNMERGE':
            r, c = map(lambda x: int(x)-1, (C[1], C[2]))
            value = bod[r][c] if bod[r][c] else []
            hap = dic[(r, c)]
            for y, x in hap:
                dic[(y, x)] = set([(y, x)])
                bod[y][x] = value if (y, x) == (r, c) else []

        if C[0] == 'PRINT':
            r, c = map(lambda x: int(x)-1, (C[1], C[2]))
            ans.append(bod[r][c] if bod[r][c] else "EMPTY")
        
    return ans