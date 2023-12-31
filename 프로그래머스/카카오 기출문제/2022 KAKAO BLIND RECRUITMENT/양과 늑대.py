from collections import defaultdict, deque

def solution(info, edges):
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    q = deque([([1, 0], {*tree[0]})])
    ans = 0
    while q:
        [sheep, wolf], children = q.popleft()
        
        if sheep == wolf:
            continue
        ans = max(ans, sheep)

        for child in children:
            next_children = {*children} - {child} | {*tree[child]}
            next_status = [sheep+1, wolf] if not info[child] else [sheep, wolf+1]
            q.append((next_status, next_children))

    return ans