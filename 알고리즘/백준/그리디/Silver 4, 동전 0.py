N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)][::-1]

ans = 0
for coin in coins:
    quotient = K // coin
    K -= coin * quotient
    ans += quotient
print(ans)