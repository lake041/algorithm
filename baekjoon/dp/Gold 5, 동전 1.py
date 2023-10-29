# https://www.acmicpc.net/problem/2293
# 재귀 시간초과

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()
dp = [1] + [0]*K

for i in range(0, N):
    if coins[i] > K:
        break
    for j in range(1, K+1):
        if j-coins[i] >= 0:
            dp[j] += dp[j-coins[i]]
print(dp[K])

'''
    1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1   1   -> one 포함
2   0   1   1   2   2   3   3   4   4   5   -> two 반드시 포함
5   0   0   0   0   1   1   2   2   3   4   -> five 반드시 포함
    1   2   2   3   4   5   6   7   8   10  -> dp[]
'''

# # 재귀 시간초과
# N, K = map(int, input().split())
# coins = [int(input()) for _ in range(N)]
# coins.sort(reverse=True)

# count = 0
# def recur(target, coins):
#     global count
#     if target == 0:
#         count += 1
#         return
#     if target < coins[0]:
#         return
#     if len(coins) == 1:
#         if target % coins[0] == 0:
#             count += 1
#         return
#     quotient = target//coins[0]
#     for i in range(quotient+1):
#         recur(target-coins[0]*i, coins[1:])

# for coin in coins:
#     if coin > K:
#         coins = coins[1:]
#     else:
#         break
# recur(K, coins)
# print(count)