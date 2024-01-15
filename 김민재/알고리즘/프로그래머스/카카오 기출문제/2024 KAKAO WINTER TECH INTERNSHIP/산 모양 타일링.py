def solution(N, tops):
    MOD = 10007
    
    dp = {}
    dp[0] = [3, 1] if tops[0]==1 else [2, 1]
    for i in range(1, N):
        if tops[i]==1:
            dp[i] = [
                (dp[i-1][0]*3 + dp[i-1][1]*2)%MOD,
                (dp[i-1][0]*1 + dp[i-1][1]*1)%MOD
                ]
        else:
            dp[i] = [
                (dp[i-1][0]*2 + dp[i-1][1]*1)%MOD,
                (dp[i-1][0]*1 + dp[i-1][1]*1)%MOD
                ]

    return sum(dp[N-1])%MOD