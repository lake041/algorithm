# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())
weight, value = {}, {}
weight[0], value[0] = 0, 0
for i in range(1, N+1):
    W, V = map(int, input().split())
    weight[i] = W
    value[i] = V

'''
핵심 점화식
dp[n][k] = max(dp[n-1][k], dp[n-1][k-weight[n]] + value[n])

dp[n][k]: n번 물건까지 사용해서 무게 k까지 채웠을 때의 최대 value

(1) n번 물건 사용 X => n-1번 물건까지 사용해서 무게 k까지 채워야한다.
(2) n번 물건 사용 O => n번 물건의 무게를 제외한 나머지 무게 k-weight[n]을 n-1번 물건까지 사용하여 채워야한다.
'''

dp = [[0] * (K+1) for _ in range(N+1)]
for n in range(1, N+1):
    for k in range(1, K+1):
        if k - weight[n] >= 0:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-weight[n]] + value[n])
        else:
            dp[n][k] = dp[n-1][k]
print(dp[N][K])