# N = 500이므로 전부 다 구하면 된다.

from sys import maxsize

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

def cal(m1, m2):
    a, b = m1
    _, d = m2
    return a * b * d

for interval in range(1, N):
    for start in range(N-interval):
        if interval == 1:
            dp[start][start+interval] = M[start][0]*M[start][1]*M[start+interval][1]
            continue
        dp[start][start+interval] = maxsize
        for k in range(start, start+interval):
            dp[start][start+interval] = min(
                dp[start][start+interval],
                dp[start][k] + dp[k+1][start+interval] + M[start][0]*M[k][1]*M[start+interval][1]
            )

print(dp[0][N-1])