# https://www.acmicpc.net/problem/1654

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

left = 1
right = max(lans)

result = 0
while left <= right:
    mid = (left + right) // 2
    sum_ = sum([lan//mid if lan>=mid else 0 for lan in lans])

    if N <= sum_:
        # if 조건을 만족시키는 mid 중 가장 오른쪽 값을 반환한다.
        result = mid
        left = mid + 1
    elif N > sum_:
        right = mid - 1
print(result)