def solution(storey):
    ans = 100_000_000

    def dfs(storey, cnt, k):
        nonlocal ans
        if not storey:
            ans = min(ans, cnt)
            return
    
        if cnt > ans:
            return
            
        last = storey % 10
        dfs((storey-last)//10, cnt + last, k+1)
        dfs((storey+(10-last))//10, cnt + 10 - last, k+1)
    
    dfs(storey, 0, 0)
    
    return ans