N = int(input())
nums = list(map(int, input().split()))
up, down = [0]*N, [0]*N

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i] and up[j]+1 > up[i]:
            up[i] = up[j] + 1

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if nums[i] > nums[j] and down[i] < down[j]+1:
            down[i] = down[j] + 1

print(max(up[i]+down[i]+1 for i in range(N)))