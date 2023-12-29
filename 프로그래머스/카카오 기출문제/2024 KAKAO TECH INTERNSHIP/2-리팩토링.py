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

    # python에서 함수 밖의 list, set, dict 같은 mutable 객체들은 따로 파라미터로 받지 않아도 바로 참조할 수 있다.
    # mutable 객체들은 메모리에 저장된 위치를 참조하기 때문이다.
    # 숫자, 문자열, 튜플 등이 불변 객체에 속한다.
    # 이들은 객체의 내용을 변경하려고 하면 새로운 객체가 생성된다.
    # immutable 객체: Call by Value
    # mutable 객체: Call by Reference
    def bfs(i):
        q = deque([i])
        visited[i] = True
        while q:
            node = q.popleft()
            if not go[node]: # 막대
                ans[2] += 1
                break
            if len(go[node])==2 and len(take[node])==2: # 8자
                ans[3] += 1
                break
            for next_node in go[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node) 
        ans[1] += 1

    for i in next:
        bfs(i)

    return ans