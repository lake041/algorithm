from sys import setrecursionlimit
setrecursionlimit(100000)

def find_parents(tree, cur, parents):
    parent = tree[cur]["parent"]
    if not parent:
        return
    parents.append(parent)
    find_parents(tree, parent, parents)

T = int(input())
for _ in range(T):
    N = int(input())
    
    tree = [{ "parent":0, "child":[] } for _ in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        tree[B]["parent"] = A
        tree[A]["child"].append(B)
    
    target_a, target_b = map(int, input().split())
    parent_a, parent_b = [target_a], [target_b]

    find_parents(tree, target_a, parent_a)
    find_parents(tree, target_b, parent_b)

    while parent_a and parent_b and parent_a[-1] == parent_b[-1]:
        ans = parent_a[-1]
        parent_a.pop()
        parent_b.pop()

    print(ans)