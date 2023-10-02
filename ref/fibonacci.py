T = int(input())
nums = [int(input()) for _ in range(T)]
dp = {0:[1, 0], 1:[0, 1]}
for i in range(41):
	if i in dp:
		continue
	dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

for num in nums:
	print(dp[num][0], dp[num][1])

'''
fibo(3) = fibo(2) + fibo(1)
        = fibo(1) + fibo(0) + fibo(1)
        = 1 + 0 + 1
0이 나온 횟수: fibo(2) 나온 횟수
1이 나온 횟수: fibo(1) 나온 횟수
'''