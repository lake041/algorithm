'''
4       5       6
xooo    xxooo   xxooox
xxxx    xooox   xoooxx
ooox    oooxx   oooooo
'''

def solution(n):
    MOD = 1_000_000_007
    
    dp = [0]*100_001
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 3, 10
    
    # memo[k] = dp[k] + dp[k-3] + dp[k-6] + ... +
    memo = [0]*100_001
    memo[0], memo[1], memo[2], memo[3] = 1, 1, 3, 11
    
    # 한 번에 MOD 하는 게 더 빠르다.
    for k in range(4, 100_001):
        dp[k] = (dp[k-1] + dp[k-2]*2 + dp[k-3]*5
                + memo[k-4]*2
                + (memo[k-5]*2 if k>=5 else 0)
                + (memo[k-6]*4 if k>=6 else 0)) % MOD
        memo[k] = (dp[k] + memo[k-3]) % MOD
                
    return dp[n]