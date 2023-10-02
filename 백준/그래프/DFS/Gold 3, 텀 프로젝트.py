import sys
from collections import Counter
sys.setrecursionlimit(100000)

T = int(input())
for _ in range(T):
    N = int(input())
    graph = list(map(lambda x: int(x)-1, input().split()))
    check = [False]*N
    
    def dfs(start, now, team: set):
        next = graph[now]
        team.add(now)
        if next == start:
            for student in team:
                check[student] = True
            return
        elif next in team:
            return
        else:
            dfs(start, next, team)

    for student in graph:
        if check[student] == True:
            continue
        dfs(student, student, set())
    
    print(Counter(check)[False])

'''
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8

3
0
'''