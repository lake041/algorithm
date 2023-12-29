def solution(sizes):
    R, C = 0, 0
    
    for row, col in sizes:
        R = max(max(row, col), R)
        C = max(min(row, col), C)
    
    return R * C