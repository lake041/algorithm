# https://www.acmicpc.net/problem/15649

def go(index):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, N+1):
        if check[i] == True:
            continue
        check[i] = True
        ans[index] = i
        go(index+1)
        check[i] = False

N, M = map(int, input().split())
check = [False]*(N+1)
ans = [0]*M
go(0)