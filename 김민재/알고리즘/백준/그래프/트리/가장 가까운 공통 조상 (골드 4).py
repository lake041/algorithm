def find_parents(memo, now, parents):
    while memo[now]:
        parents.append(memo[now])
        now = memo[now]

T = int(input())
for _ in range(T):
    N = int(input())
    
    memo = [0]*(N+1)
    for _ in range(N-1):
        A, B = map(int, input().split())
        memo[B] = A
    
    target_a, target_b = map(int, input().split())
    parent_a, parent_b = [target_a], [target_b]

    find_parents(memo, target_a, parent_a)
    find_parents(memo, target_b, parent_b)

    while parent_a and parent_b and parent_a[-1] == parent_b[-1]:
        ans = parent_a[-1]
        parent_a.pop()
        parent_b.pop()

    print(ans)