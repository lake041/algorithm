# https://www.acmicpc.net/problem/12920

# 메모리 초과 뜬다.
'''
N, M = map(int, input().split())
weight, value = {0:0}, {0:0}
total = 0
idx = 1
for _ in range(N):
    W, V, K = map(int, input().split())
    for _ in range(K):
        weight[idx], value[idx] = W, V
        idx += 1
        total += 1

dp = [[0] * (M+1) for _ in range(total+1)]
for n in range(1, total+1):
    for k in range(1, M+1):
        if k - weight[n] >= 0:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-weight[n]] + value[n])
        else:
            dp[n][k] = dp[n-1][k]
print(dp[total][M])
'''

# 시간 초과
'''
N, M = map(int, input().split())
weight, value, number = {0:0}, {0:0}, {0:0}
for i in range(1, N+1):
    W, V, K = map(int, input().split())
    weight[i], value[i], number[i] = W, V, K

dp = [[0] * (M+1) for _ in range(N+1)]
for n in range(1, N+1):
    for m in range(1, M+1):
        dp[n][m] = max(
                [
                dp[n-1][m-weight[n]*num] + value[n]*num
                for num in range(min(m//weight[n], number[n])+1)
                ]
            )
print(dp[N][M])
'''

# PyPy3 통과
# 이진 분해
# 플래티넘은 건들지말자

N, M = map(int, input().split())
weight, value = {0:0}, {0:0}
idx = 1
for _ in range(N):
    W, V, K = map(int, input().split())
    k = 1
    while K >= k:
        weight[idx], value[idx] = W*k, V*k
        K -= k
        k *= 2
        idx += 1

    # ⭐️
    if K > 0:
        weight[idx], value[idx] = W*K, V*K
        idx += 1
total = idx - 1

dp = [[0] * (M+1) for _ in range(total+1)]
for n in range(1, total+1):
    for k in range(1, M+1):
        if k - weight[n] >= 0:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-weight[n]] + value[n])
        else:
            dp[n][k] = dp[n-1][k]
print(dp[total][M])
