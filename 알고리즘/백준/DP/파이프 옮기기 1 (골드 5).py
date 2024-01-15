from itertools import product

N = int(input())
bod = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for y, x in product(range(N), range(N)):
    if (y, x) in [(0, 0), (0, 1)]:
        continue
    RtoR = dp[y][x-1][0] if x-1 >= 0 else 0
    DtoR = dp[y][x-1][1] if x-2 >= 0 and y-1 >= 0 else 0
    RtoD = dp[y-1][x-1][0] if y-1 >= 0 and x-2 >= 0 else 0
    DtoD = dp[y-1][x-1][1] if y-2 >= 0 and x-2 >= 0 else 0
    UtoD = dp[y-1][x-1][2] if y-2 >= 0 and x-1 >= 0 else 0
    DtoL = dp[y-1][x][1] if y-2 >= 0 and x-1 >= 0 else 0
    LtoL = dp[y-1][x][2] if y-2 >= 0 else 0
    
    dp[y][x][0] = RtoR + DtoR if not bod[y][x] else 0
    dp[y][x][1] = RtoD + DtoD + UtoD if not bod[y][x] and not bod[y-1][x] and not bod[y][x-1] else 0
    dp[y][x][2] = DtoL + LtoL if not bod[y][x] else 0

print(sum(dp[-1][-1]))
