def solution(n):
    MOD =  1_000_000_007
    dp = {1:1, 2:2}
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[n]