from sys import setrecursionlimit
setrecursionlimit(1_000_000)

T = int(input())
for _ in range(T):
    N = int(input())
    checked = [False]*N
    target = list(map(lambda x: int(x)-1, input().split()))
    ans = N

    def dfs(start, now, team: list, team_set: set):
        global ans
        if checked[now] == True:
            return
        
        team.append(now)
        team_set.add(now)
        checked[now] = True
        if target[now] == start:
            ans -= len(team)
        # set으로 검색을 수행해서 시간복잡도를 줄이고나서야 통과됐다.
        elif target[now] in team_set:
            new_start = target[now]
            start_index = team.index(new_start)
            ans -= len(team)-start_index
        else:
            dfs(start, target[now], team, team_set)

    for i in range(N):
        dfs(i, i, [], set())

    print(ans)

'''
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''