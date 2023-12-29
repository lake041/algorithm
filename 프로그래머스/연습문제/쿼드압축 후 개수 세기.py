from itertools import product

def solution(bod):
    ans = [0, 0]
    
    def dfs(sy, sx, length):
        if any(bod[y][x] != bod[sy][sx] for y, x in product(range(sy, sy+length), range(sx, sx+length))):
            dfs(sy, sx, length//2)
            dfs(sy+length//2, sx, length//2)
            dfs(sy, sx+length//2, length//2)
            dfs(sy+length//2, sx+length//2, length//2)
        else:
            ans[bod[sy][sx]] += 1
    
    dfs(0, 0, len(bod))

    return ans