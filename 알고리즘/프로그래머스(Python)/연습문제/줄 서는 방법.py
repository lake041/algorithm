def solution(n, k):
    facto = [1]
    for num in range(1, n+1):
        facto.append(facto[-1] * num)
    
    ans = []
    
    def dfs(pool, l, k):
        if not pool:
            return
        index = (k-1) // facto[l-1]
        ans.append(pool[index])
        pool.remove(pool[index])
        dfs(pool, l-1, k - facto[l-1] * index )
    
    dfs(list(range(1, n+1)), n, k)
    
    return ans