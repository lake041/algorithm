M, N = map(int, input().split())
needs = sorted(int(input()) for _ in range(N))
candy = sum(needs) - M

MOD = 2**64
ans = 0

for index, need in enumerate(needs):
    need = min(need, candy//(N-index))
    candy -= need
    ans += need ** 2 % MOD

print(ans % MOD)