from itertools import product
from math import sqrt

def solution(r1, r2):
    answer = 0
    
    for x, y in product(range(1, r2), range(1, r2)):
        if r1 <= sqrt(x*x + y*y) <= r2:
            answer += 1
    answer += r2 - r1 + 1
    answer *= 4
                        
    return answer