from collections import defaultdict, deque

def solution(edges):
    N = len(edges) + 1
    go = defaultdict(set)
    take = defaultdict(set)
    for a, b in edges:
        a, b = a-1, b-1
        go[a].add(b)
        take[b].add(a)

    start = -2
    for node in range(1_000_002):
        if len(take[node])==0 and len(go[node])>=2:
            start = node
            break


    # 시작, 도넛, 막대, 8자
    ans = [start+1, 0, 0, 0]
    next = go[start]

    for i in next:
        take[i].remove(start)

    visited = [False]*N
    for i in next:
        q = deque([i])
        visited[i] = True
        find = False
        while q:
            node = q.popleft()
            if not go[node]: # 막대
                ans[2] += 1
                find = True
                break
            if len(go[node])==2 and len(take[node])==2: # 8자
                ans[3] += 1
                find = True
                break
            for next_node in go[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node) 
        if not find:
            ans[1] += 1

    return ans