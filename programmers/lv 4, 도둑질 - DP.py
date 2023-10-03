def solution(money):
    answer = 0
    # start 훔치고 end 안 훔친 경우 => next 훔칠 수 있음
    # start 안 훔치고 end 훔친 경우 => next 훔칠 수 없음
    # start 안 훔치고 end 안 훔친 경우 => next 훔칠 수 있음
    dp = {
        0: [0, 0, 0], 
        1: [0, 0, 0],
        2: [money[0], money[2], money[1]],
        3: [money[0]+money[2], money[1]+money[3], max(money[1], money[2])]
    }
    for i in range(4, len(money)):
        dp[i] = [
            max(dp[i-1][0], dp[i-2][0] + money[i-1]),
            dp[i-1][2] + money[i],
            max(dp[i-1][1], dp[i-1][2]),
        ]
    answer = max(dp[len(money)-1])
    
    return answer