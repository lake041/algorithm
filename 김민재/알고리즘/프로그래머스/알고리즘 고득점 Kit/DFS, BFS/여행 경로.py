# 초기 풀이: 시간복잡도가 굉장히 큼. 애초에 왜 통과했는지 이해가 안 됨.
# 테스트 1: 1200ms
from collections import deque

def solution(tickets):
    answer = ["ZZZ"]
    
    q = deque()
    q.append(["ICN", ["ICN"], []])
    while q:
        now, routes, visited = q.popleft()
        if len(routes) == len(tickets) + 1:
            answer = min(answer, routes)
            continue

        for i in range(len(tickets)):
            if i in visited:
                continue
            start, dest = tickets[i]
            if now == start:
                q.append([dest, routes+[dest], visited+[i]])
    
    return answer


# 새로운 풀이 1: BFS
# 테스트 1: 380ms
from collections import deque, defaultdict

def solution(tickets):
    L = len(tickets)
    tickets.sort()

    graph = defaultdict(list)
    for index, [start, end] in enumerate(tickets):
        graph[start].append((end, index))
    
    q = deque([("ICN", ["ICN"], 0, set())])
    while q:
        cur, route, cnt, visited = q.popleft()
        
        if cnt == L:
            return route
        
        for next_node, index in graph[cur]:
            if index in visited:
                continue
            q.append((next_node, route + [next_node], cnt+1, visited | {index}))



#  새로운 풀이 2: DFS
# 테스트 1: 0.03ms
from collections import defaultdict

def solution(tickets):
    L = len(tickets)
    tickets.sort()

    graph = defaultdict(list)
    for index, [start, end] in enumerate(tickets):
        graph[start].append((end, index))
    
    visited = [False]*L
    
    def dfs(cur, route, depth):
        if depth == L:
            return route
        
        for next_node, index in graph[cur]:
            if visited[index]:
                continue

            visited[index] = True
            answer = dfs(next_node, route+[next_node], depth+1)
            visited[index] = False

            if answer:
                return answer

    return dfs("ICN", ["ICN"], 0)
