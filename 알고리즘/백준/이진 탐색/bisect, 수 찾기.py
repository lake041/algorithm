# https://www.acmicpc.net/problem/1920

from bisect import bisect_left

N = int(input())
pool = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

# 1. 직접 구현
'''
def my_bisect(target):
    left = 0
    right = N-1

    while left <= right:
        mid = (left + right) // 2
        if pool[mid] == target:
            return print(1)
        elif target > pool[mid]:
            left = mid + 1
        elif target < pool[mid]:
            right = mid - 1
    return print(0)

for num in nums:
    my_bisect(num)
'''

# 2. 라이브러리
for num in nums:
    # bisect_right의 경우, 그 값의 가장 오른쪽 인덱스의 다음 위치를 반환한다.
    index = bisect_left(pool, num)
    if index!=len(pool) and pool[index]==num:
        print(1)
    else:
        print(0)
