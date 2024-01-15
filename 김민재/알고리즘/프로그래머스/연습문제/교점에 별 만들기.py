from itertools import combinations

def solution(lines):
    dots = set()
    for i, j in combinations(lines, 2):
        a, b, e = i
        c, d, f = j
        
        if not a*d - b*c:
            continue
        
        x = (b*f - e*d) / (a*d - b*c) 
        y = (e*c - a*f) / (a*d - b*c)
        
        if float(x).is_integer() and float(y).is_integer():
            dots.add((int(x), int(y)))

    max_x, min_x = max(dot[0] for dot in dots), min(dot[0] for dot in dots)
    max_y, min_y = max(dot[1] for dot in dots), min(dot[1] for dot in dots)

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    dots = [(abs(y - max_y), abs(x - min_x)) for x, y in dots]
    
    bod = [["."]*width for _ in range(height)]
    for y, x in dots:
        bod[y][x] = "*"
    bod = [''.join(row) for row in bod]
    
    return bod