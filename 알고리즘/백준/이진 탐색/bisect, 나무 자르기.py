# https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

result = 0
while left <= right:
    mid = (left + right) // 2
    sum_ = sum([tree-mid if tree>=mid else 0 for tree in trees])

    if M <= sum_:
        # if 조건을 만족시키는 mid 중 가장 오른쪽 값을 반환한다.
        result = mid
        left = mid + 1
    elif M > sum_:
        right = mid - 1
print(result)