'''
xy = yellow
xy + 2x + 2y + 4 = brown + yellow
x + y = (brown - 4)//2
'''

def solution(brown, yellow):
    r_plus_c = (brown-4)//2
    r_mul_c = yellow
    
    for i in range(1, r_plus_c):
        if i * (r_plus_c-i) == r_mul_c:
            r = max(i, (r_plus_c-i)) + 2
            c = min(i, (r_plus_c-i)) + 2
    
    answer = [r, c]
    return answer