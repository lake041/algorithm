from sys import maxsize

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right, subtotal = 0, 0, nums[0]
ans = maxsize

while True:
    if subtotal >= S:
        ans = min(ans, right-left+1)
        subtotal -= nums[left] 
        left += 1
    elif right == N-1:
        break
    else:
        right += 1
        subtotal += nums[right]

print(0 if ans == maxsize else ans)