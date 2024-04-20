from itertools import combinations

def solution(s):
    ans = 0
    for start, end in combinations(range(len(s)+1), 2):
        x = s[start:end] 
        if x == x[::-1]:
            ans = max(ans, end-start)
    return ans