def solution(s):
    s = s[2:-2]
    s = list(s.split(sep = "},{"))
    
    dp = {}
    for nums in s:
        nums = list(map(int, nums.split(sep = ",")))
        dp[len(nums)] = nums
    
    ans = []
    cur = 1
    while True:
        if cur not in dp:
            break
        for num in dp[cur]:
            if num not in ans:
                ans.append(num)
        cur += 1
    
    return ans