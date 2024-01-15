from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(now, cur_cost, costs, visited):
    costs[now] = cur_cost
    visited.add(now)
    for node, cost in graph[now]:
        if node not in visited:
            dfs(node, cur_cost+cost, costs, visited)

costs = [0]*(N+1)
dfs(1, 0, costs, set())
farthest = costs.index(max(costs))

costs = [0]*(N+1)
dfs(farthest, 0, costs, set())
farthest_cost = max(costs)

print(farthest_cost)