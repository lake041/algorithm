from sys import stdin
input = stdin.readline

N = int(input())
infos = [list(input().split())[1:] for _ in range(N)]
dic = {} # 재귀 때문에 defaultdict 의미 없다

def trie(dic, arr):
    if not arr:
        return
    if arr[0] not in dic:
        dic[arr[0]] = {}
        trie(dic[arr[0]], arr[1:])

def dfs(dic, level):
    if not dic:
        return
    for child in sorted(dic.keys()):
        print('--'*level + child)
        dfs(dic[child], level+1)

for info in infos:
    trie(dic, info)

dfs(dic, 0)