# 이해는 되지만 체화는 멀었다
# 일단 암기하고 다음에 다시 풀어보자

'''
중위 순회 : 7 3 8 1 9 4 10 // "0" // 11 5 2 6
후위 순회 : 7 8 3 9 10 4 1 // 11 5 6 2 // "0"
'''

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index = [0]*(N+1)
for i in range(N):
    index[inorder[i]] = i

def preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return    
    root = postorder[post_end]
    print(root, end = " ")

    left_node = index[root] - in_start
    right_node = in_end - index[root]
    preorder(in_start, in_start+(left_node-1), post_start, post_start+(left_node-1))
    preorder(in_end-(right_node-1), in_end, post_end-(right_node), post_end-1)

preorder(0, N-1, 0, N-1)