# https://www.acmicpc.net/problem/1191

from sys import stdin
input = stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    mid, left, right = input().rstrip().split()
    tree[mid] = [left, right]

def preorder(mid):
    if mid != '.':
        print(mid, end='')
        preorder(tree[mid][0])
        preorder(tree[mid][1])

def inorder(mid):
    if mid != '.':
        inorder(tree[mid][0])
        print(mid, end='')
        inorder(tree[mid][1])

def postorder(mid):
    if mid != '.':
        postorder(tree[mid][0])
        postorder(tree[mid][1])
        print(mid, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
