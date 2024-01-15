from collections import defaultdict

N = int(input())
MOD = 1_000_000_000

# dp[(길이, 끝자리수, 비트마스크)] = 개수
# 비트마스크 9 8 7 6 5 4 3 2 1 0 등장 여부
dp = defaultdict(int)
for last in range(1, 10):
    dp[(1, last, 1<<last)] = 1

for L in range(2, N+1):
    for last in range(10):
        for B in range(1024):
            # 100 -> 101이 된 경우랑, 101 -> 101 된 경우랑 겹치므로 += 해야함
            if last == 0:
                dp[(L, last, B | 1<<last)] += dp[(L-1, last+1, B)] # 1 -> 0
            elif last == 9:
                dp[(L, last, B | 1<<last)] += dp[(L-1, last-1, B)] # 8 -> 9
            else:
                dp[(L, last, B | 1<<last)] += dp[(L-1, last+1, B)] + dp[(L-1, last-1, B)]
            dp[(L, last, B | 1<<last)] %= MOD

print(sum(dp[(N, i, 1023)] for i in range(10)) % MOD)

# 제시값 126461847755
# 출력값    461847755
# example = 0
# for L in range(1, 41):
#     example += sum(dp[(L, last, 1023)] for last in range(10))
# print(example % mod)

'''
N = 11
8(9876543210)
(9876543210)1
1(0123456789)
'''