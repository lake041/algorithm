from sys import stdin
from collections import defaultdict
input = stdin.readline

N = int(input())
infos = [list(input().split())[1:] for _ in range(N)]
tree = defaultdict(set)

for info in infos:
    parent = "root"
    for index, string in enumerate(info):
        tree[parent].add((parent, string, index))
        parent = (parent, string, index)

# 틀렸던 코드
'''
for info in infos:
    for index in range(len(info)):
        if index == 0:
            tree["root"].add(("root", info[index], 0))
        else:
            grand = "root" if index == 1 else info[index-2]
            parent, child = info[index-1], info[index]
            tree[(grand, parent, index-1)].add((parent, child, index))
'''

for key in tree:
    tree[key] = sorted(tree[key])

def dfs(parent_key):
    _, name, level = parent_key
    print("--"*level + name)
    for child in tree[parent_key]:
        dfs(child)

for child in tree["root"]:
    dfs(child)

# 반례
'''
5
2 KIWI BANANA
2 KIWI APPLE
4 APPLE APPLE APPLE CHERRY
4 KIWI APPLE APPLE BANANA
3 APPLE BANANA KIWI
'''