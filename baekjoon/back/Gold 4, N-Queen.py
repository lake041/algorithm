# https://www.acmicpc.net/problem/9663

N = int(input())
Q = [-1]*N
ans = 0

def go(index):
    global ans
    if index == N:
        ans += 1
        return
    
    for num in range(N):
        # 같은 행이라면
        if num in Q:
            continue

        Q[index] = num
        ok = True
        for k in range(index):
            # 행의 차이가 열의 차이와 같다면
            if abs(k-index) == abs(Q[k]-num):
                ok = False
                break        
        if ok:
            go(index+1)
        Q[index] = -1

go(0)
print(ans)
