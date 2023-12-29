def solution(money):
    # 1. start 훔치고 end 안 훔친 경우 => next 훔칠 수 없음
    # 2. start 안 훔치고 end 훔친 경우 => next 훔칠 수 없음
    # 3. start 안 훔치고 end 안 훔친 경우 => next 훔칠 수 있음
    dp = {
        3: [money[0], money[2], money[1]],
        4: [money[0]+money[2], money[1]+money[3], max(money[1], money[2])]
    }

    L = len(money)
    for i in range(5, L+1):
        dp[i] = [
            max(dp[i-2][0]+money[i-2], dp[i-1][0]),
            dp[i-1][2] + money[i-1],
            max(dp[i-1][1], dp[i-1][2])
        ]
    
    return max(dp[L])