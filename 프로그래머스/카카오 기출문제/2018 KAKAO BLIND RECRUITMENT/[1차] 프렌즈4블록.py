from itertools import product

def solution(R, C, bod):
    bod = [list(row) for row in bod]
    ans = 0
    while True:
        delete = set()
        for y, x in product(range(R-1), range(C-1)):
            if not bod[y][x]:
                continue
                
            if bod[y][x]==bod[y][x+1]==bod[y+1][x]==bod[y+1][x+1]:
                delete.update([(y, x), (y, x+1), (y+1, x), (y+1, x+1)])
        
        if not delete:
            break
            
        for y, x in delete:
            bod[y][x] = None
            ans += 1
        
        for col in range(C):
            temp = [bod[row][col] for row in range(R)]
            while None in temp:
                temp.remove(None)
            for row in range(R-1, -1, -1):
                bod[row][col] = temp.pop() if temp else None            
        
    return ans