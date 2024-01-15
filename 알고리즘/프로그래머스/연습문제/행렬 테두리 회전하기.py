from collections import deque
from itertools import count, product

def solution(R, C, queries):
    bod = [[0]*C for _ in range(R)]
    
    c = count(1)
    for y, x in product(range(R), range(C)):
        bod[y][x] = next(c)
    
    def rotate(y1, x1, y2, x2):
        q = deque()
        q.extend([bod[y1][x] for x in range(x1, x2)])
        q.extend([bod[y][x2] for y in range(y1, y2)])
        q.extend([bod[y2][x] for x in range(x2, x1, -1)])
        q.extend([bod[y][x1] for y in range(y2, y1, -1)])
        q.rotate()

        dot = deque()
        dot.extend([(y1, x) for x in range(x1, x2)])
        dot.extend([(y, x2) for y in range(y1, y2)])
        dot.extend([(y2, x) for x in range(x2, x1, -1)])
        dot.extend([(y, x1) for y in range(y2, y1, -1)])

        result = zip(list(dot), list(q))
        for (y, x), num in result:
            bod[y][x] = num

        return min(q)
    
    ans = []
    for y1, x1, y2, x2 in queries:
        ans.append(rotate(y1-1, x1-1, y2-1, x2-1))
    
    return ans