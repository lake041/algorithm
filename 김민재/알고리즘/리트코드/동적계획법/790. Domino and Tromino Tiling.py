class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        dp = {1:1, 2:2, 3:5}
        pd = {1:0, 2:1, 3:2}
        
        for i in range(4, n+1):
            dp[i] = (dp[i-1] + pd[i-1]*2 + dp[i-2]) % MOD 
            pd[i] = (pd[i-1] + dp[i-2]) % MOD
        
        return dp[n]