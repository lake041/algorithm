from math import inf

N, M = map(int, input().split())
bod = [[inf]*N for _ in range(N)]
for _ in range(M):
    y, x = map(int, input().split())
    bod[y-1][x-1] = 1
    bod[x-1][y-1] = 1

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if bod[i][j] > bod[i][k] + bod[k][j]:
                    bod[i][j] = bod[i][k] + bod[k][j]

floyd()
floyd()
floyd()
floyd()
floyd()

minValue = inf
index = inf
for i in range(N):
    temp = sum(bod[i])-bod[i][i]
    if temp < minValue:
        minValue = temp
        index = i
print(index+1)

'''
5 5
1 3
1 4
4 5
4 3
3 2
'''