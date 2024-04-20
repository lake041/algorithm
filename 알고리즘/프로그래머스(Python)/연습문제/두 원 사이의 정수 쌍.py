from math import sqrt, ceil, floor

def solution(r1, r2):
    answer = 0
    
    for y in range(1, r2+1):
        start = ceil(sqrt(r1*r1 - y*y)) if y<r1 else 0
        end = floor(sqrt(r2*r2 - y*y))
        answer += (end-start+1)
    answer *= 4
    
    return answer