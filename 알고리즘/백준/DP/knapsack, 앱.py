# https://www.acmicpc.net/problem/7579

N, M = map(int, input().split())
size = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

# 시간 초과
"""
dp[n][m]: n 메모리까지 사용해서 m 바이트 이상 확보하기 위해 필요한 최소한의 cost

1. n 메모리 활성화: dp[n-1][m]
2. n 메모리 비활성화: dp[n-1][m-size[n]] + cost[n]

dp[n][m] = min(dp[n-1][m], dp[n-1][m-size[n]] + cost[n])
그런데 N <= 100, M <= 10,000,000이므로 10억 번 연산, 시간 초과
"""

# 풀이
"""
메모리 사이즈를 열로 두면 시간 초과가 나오기 때문에 cost를 열로 두자
cost의 경우 최대 10,000까지 가능하므로 기껏해야 1,000,000번 연산한다.

dp[n][c]: n 메모리까지 사용해서 c cost 이하로 확보할 수 있는 최대 메모리
하지만 최대 메모리가 최초로 나왔을 때의 c를 반환해야 하므로 c를 행으로 두자

핵심 점화식
dp[c][n] = max(dp[c-cost[n]][n-1] + size[n], dp[c][n-1])
"""

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
max_cost = sum(cost)+1
dp = [[0]*max_cost for _ in range(n+1)]
ans = 10001

for i in range(1, n+1):
    ci, mi = cost[i], memory[i]
    for j in range(max_cost):
        dp[i][j] = dp[i-1][j]
    for j in range(ci, max_cost):
        dp[i][j] = max(dp[i-1][j-ci] + mi, dp[i][j])
        if dp[i][j] >= m:
            ans = min(ans, j)

print(ans)