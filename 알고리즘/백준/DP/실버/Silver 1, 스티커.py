# https://www.acmicpc.net/problem/9465

T = int(input())
for _ in range(T):
    N = int(input())
    bod = [list(map(int, input().split())) for _ in range(2)]
    if N == 1:
        print(max(bod[0][0], bod[0][1]))
        continue
    DP_UP = [bod[0][0], bod[1][0] + bod[0][1]]
    DP_DOWN = [bod[1][0], bod[0][0] + bod[1][1]]
    for i in range(2, N):
        DP_UP.append(max(DP_DOWN[i-1] + bod[0][i], max(DP_UP[i-2], DP_DOWN[i-2]) + bod[0][i]))
        DP_DOWN.append(max(DP_UP[i-1] + bod[1][i], max(DP_UP[i-2], DP_DOWN[i-2]) + bod[1][i]))
    print(max(DP_UP[N-1], DP_DOWN[N-1]))