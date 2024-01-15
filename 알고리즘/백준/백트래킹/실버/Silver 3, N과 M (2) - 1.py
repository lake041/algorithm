# https://www.acmicpc.net/problem/15650

def go(index, start):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, N+1):
        if check[i] == True:
            continue
        start = i+1
        check[i] = True
        ans[index] = i
        go(index+1, start)
        check[i] = False

N, M = map(int, input().split())
check = [False]*(N+1)
ans = [0]*M
go(0, 1)