from sys import maxsize

N, S = map(int, input().split())
nums = list(map(int, input().split()))
left, right, sum_ = 0, 1, nums[0]

ans = maxsize
# left 이상 right 미만
while True:
    if sum_ >= S:
        ans = min(ans, right-left)
        sum_ -= nums[left]
        left += 1
    # right == N이면서 left를 다 땡겨오고 그 다음 다시 right를 늘릴 차례에 break
    elif right == N:
        break
    else:
        sum_ += nums[right]
        right += 1

print(0 if ans == maxsize else ans)

'''
5 5
1 1 1 1 1
'''