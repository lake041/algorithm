def solution(land):
    answer = 0
    length = len(land)
    dp = {0:land[0]}

    for level in range(1, length):
        dp[level] = [
            land[level][0] + max(dp[level-1][1], dp[level-1][2], dp[level-1][3]),
            land[level][1] + max(dp[level-1][0], dp[level-1][2], dp[level-1][3]),
            land[level][2] + max(dp[level-1][0], dp[level-1][1], dp[level-1][3]),
            land[level][3] + max(dp[level-1][0], dp[level-1][1], dp[level-1][2]),
        ]

    return max(dp[length-1])