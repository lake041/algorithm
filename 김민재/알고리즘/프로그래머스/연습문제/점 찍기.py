def solution(k, d):
    return sum(1 + (d**2 - x**2)**0.5 // k for x in range(0, d+1, k))