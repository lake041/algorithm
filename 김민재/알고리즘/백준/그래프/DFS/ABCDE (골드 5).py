N, M = map(int, input().split())
friend_list = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

def dfs(cur, depth, visited):
    if depth == 4:
        return True
    
    for friend in friend_list[cur]:
        if friend not in visited:
            if dfs(friend, depth + 1, visited | {friend}):
                return True
    return False

print(1 if any(dfs(i, 0, {i}) for i in range(N)) else 0)