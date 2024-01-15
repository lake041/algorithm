from sys import stdin
input = stdin.readline

# MST
# Union-Find

N, M, K = map(int, input().split())
stones = list(map(int, input().split()))
NO = set(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M))
visited = [False]*N

def go_right(index):
    return 0 if index == N-1 else index+1

def go_left(index):
    return N-1 if index == 0 else index-1

def find_group_and_min_stones(index):
    visited[index] = True
    my_stones = [stones[index]]

    prev_left, left = index, go_left(index)
    while not visited[left] and (prev_left, left) not in NO and (left, prev_left) not in NO:
        visited[left] = True
        my_stones.append(stones[left])
        prev_left, left = left, go_left(left)

    prev_right, right = index, go_right(index)
    while not visited[right] and (prev_right, right) not in NO and (right, prev_right) not in NO:
        visited[right] = True
        my_stones.append(stones[right])
        prev_right, right = right, go_right(right)
    
    return min(my_stones)

total = 0
for i in range(N):
    if visited[i]:
        continue
    total += find_group_and_min_stones(i)

print("YES" if total <= K or M <= 1 else "NO")

# 반례
'''
5 0 0
3 3 1 3 3

5 1 0
3 3 1 3 3
1 2
'''
