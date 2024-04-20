def solution(msg):
    dp = {}
    alphas = list(range(ord('A'), ord('Z')+1))
    for index, char in enumerate(alphas):
        dp[chr(char)] = index+1
    latest = 26
    temp = ''
    ans = []
    for index, char in enumerate(msg):
        if temp+char in dp:
            temp += char
        else:
            ans.append(dp[temp])
            temp += char
            latest += 1
            dp[temp] = latest
            temp = char
    ans.append(dp[temp])
    
    return ans