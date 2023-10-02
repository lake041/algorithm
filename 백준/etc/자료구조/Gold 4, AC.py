from collections import deque
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    P = list(input().rstrip())
    N = int(input())
    nums = input().rstrip()
    nums = nums[1:-1]
    if len(nums) == 0:
        nums = []
    else:
        nums = deque(nums.split(','))
    error = False
    count = 0
    for op in P:
        if op == 'R':
            count += 1
        if op == 'D':
            if len(nums)==0:
                error = True
                break
            if count % 2 == 1:
                nums.pop()
            else:
                nums.popleft()
    if error:
        print('error')
    else:
        if count % 2 == 1:
            nums.reverse()
        ans = '['
        ans += ','.join(map(str, nums)) + ']'
        print(ans)
