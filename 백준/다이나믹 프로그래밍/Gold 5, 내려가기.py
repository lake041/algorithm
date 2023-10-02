# https://www.acmicpc.net/problem/2096

from sys import stdin
input = stdin.readline

N = int(input())
stair = list(map(int, input().split()))
for i in range(3):
    stair[i] = [stair[i], stair[i]]

for _ in range(N-1):
    temp = list(map(int, input().split()))
    temp0 = [
        temp[0] + max(stair[0][0], stair[1][0]),
        temp[0] + min(stair[0][1], stair[1][1])
    ]
    temp1 = [
        temp[1] + max(stair[0][0], stair[1][0], stair[2][0]),
        temp[1] + min(stair[0][1], stair[1][1], stair[2][1])
    ]
    temp2 = [
        temp[2] + max(stair[1][0], stair[2][0]),
        temp[2] + min(stair[1][1], stair[2][1])
    ]
    stair = [temp0, temp1, temp2]

print(max([x[0] for x in stair]), min([x[1] for x in stair]))


# # 메모리 초과
# stair = [list(map(int, input().split())) for _ in range(N)]
# stair[0][0] = [stair[0][0], stair[0][0]]
# stair[0][1] = [stair[0][1], stair[0][1]]
# stair[0][2] = [stair[0][2], stair[0][2]]

# for i in range(1, N):
#     temp0 = []
#     temp0.append(stair[i][0] + max(stair[i - 1][0][0], stair[i - 1][1][0]))
#     temp0.append(stair[i][0] + min(stair[i - 1][0][1], stair[i - 1][1][1]))
#     stair[i][0] = temp0

#     temp1 = []
#     temp1.append(stair[i][1] + max(stair[i - 1][0][0], stair[i - 1][1][0], stair[i - 1][2][0]))
#     temp1.append(stair[i][1] + min(stair[i - 1][0][1], stair[i - 1][1][1], stair[i - 1][2][1]))
#     stair[i][1] = temp1

#     temp2 = []
#     temp2.append(stair[i][2] + max(stair[i - 1][1][0], stair[i - 1][2][0]))
#     temp2.append(stair[i][2] + min(stair[i - 1][1][1], stair[i - 1][2][1]))
#     stair[i][2] = temp2

# print(max([x[0] for x in stair[N - 1]]), min([x[1] for x in stair[N - 1]]))
