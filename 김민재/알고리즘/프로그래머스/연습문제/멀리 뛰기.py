def solution(n):
    dp = {1:1, 2:2, 3:3, 4:5}
    for i in range(5, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1234567
    return dp[n]