from collections import defaultdict, deque

def solution(info, edges):
    status = [1, 0]
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    q = deque([(0, [1, 0], {*tree[0]}, [0])])
    ans = 0
    while q:
        cur, [sheep, wolf], children, route = q.popleft()
        
        if sheep == wolf:
            continue
        ans = max(ans, sheep)

        for child in children:
            next_children = set(children) - {child} | {*tree[child]}
            next_status = [sheep+1, wolf] if not info[child] else [sheep, wolf+1]
            q.append((child, next_status, next_children, route+[child]))

    return ans