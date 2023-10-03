N, M = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]

DP = [[0]*(N+1) for _ in range(N+1)]
for row in range(1, N+1):
    for col in range(1, N+1):
        DP[row][col] = DP[row][col-1] + DP[row-1][col] - DP[row-1][col-1] + bod[row-1][col-1]

for _ in range(M):
    row1, col1, row2, col2 = map(int, input().split())
    print(DP[row2][col2] - DP[row2][col1-1] - DP[row1-1][col2] + DP[row1-1][col1-1])

'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
'''