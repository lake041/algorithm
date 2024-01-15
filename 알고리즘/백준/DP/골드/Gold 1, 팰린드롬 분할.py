S = input()
L = len(S)

# dp[N] => S[0:N]
dp = [0]
for index in range(1, L+1):
    next = dp[index-1] + 1
    # [0:j] + [j:index]
    for j in range(index-1):
        if S[j:index] == S[j:index][::-1]:
            next = min(next, dp[j] + 1)
    dp.append(next)
print(dp[L])

'''
BBCDDECAECBDABADDCEBACCCBDCAABDBADD
22
'''