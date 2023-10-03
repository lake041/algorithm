from itertools import product
from math import sqrt

def solution(r1, r2):
    answer = 0
    max_ = r2*r2
    min_ = r1*r1
    
    for y in range(1, r2):
        for x in range(1, r2):
            dist = x*x + y*y
            if dist < min_:
                continue
            elif min_ <= x*x + y*y <= max_:
                answer += 1
            else:
                break
    answer += r2 - r1 + 1
    answer *= 4
                
    return answer