# 1번 그룹이랑 연결된 건 모두 2번 그룹
# 2번 그룹이랑 연결된 건 모두 1번 그룹
# 티키타카 하면서 끝까지 이어진다면 YES 아니면 NO
# dfs의 return 값을 만족하면 True 아니면 False로 둔다.

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    a = [[] for _ in range(V+1)]
    color = [0]*(V+1)
    for _ in range(E):
        n, m = map(int, input().split())
        a[n].append(m)
        a[m].append(n)
    
    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:
                if dfs(y, 3-c) == False:
                    return False
            elif color[y] == color[x]:
                return False
        return True
    
    ans = True
    for i in range(V+1):
        if color[i] == 0:
            # dfs(i, 1)이 True이면 ans가 False였다가 다시 True가 된다.
            # 단 한 번이라도 False이면 그것을 유지해야한다.
            if dfs(i, 1) == False:
                ans = False
    print('YES' if ans else 'NO')