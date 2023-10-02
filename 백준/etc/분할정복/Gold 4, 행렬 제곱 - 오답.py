from copy import deepcopy

N, B = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]

# deepcopy를 사용하여 ans와 M이 동일한 값을 가지게 한 후에 ans를 변경하면 M도 변경되므로 원래의 행렬 정보를 잃게 된다.
ans = deepcopy(M)
for k in range(B):
    temp = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            result = 0
            for i in range(N):
                result += ans[row][i] * M[i][col]
            temp[row][col] = result
    ans = temp
    print(k)
    for row in ans:
        print(row)