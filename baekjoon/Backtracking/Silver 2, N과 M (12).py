# https://www.acmicpc.net/problem/15666

N, M = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()
len_nums = len(nums)
ans = [0]*M

def go(index, start):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, len_nums):
        ans[index] = nums[i]
        go(index+1, i)

go(0, 0)