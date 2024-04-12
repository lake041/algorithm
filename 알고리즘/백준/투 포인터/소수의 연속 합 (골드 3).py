N = int(input())
prime = [True]*(N+1)

for i in range(2, int(N**0.5)+1):
    if not prime[i]:
        continue
    j = 2
    while i*j <= N:
        prime[i*j] = False
        j += 1

nums = [i for i in range(2, N+1) if prime[i]]

cnt = 0
right = 0
tum = 0
end = len(nums)

for left in range(end):
    while tum < N and right < end:
        tum += nums[right]
        right += 1
    if tum == N:
        cnt += 1
    tum -= nums[left]

print(cnt)