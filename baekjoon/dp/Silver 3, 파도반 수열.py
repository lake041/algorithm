# P(N) = P(N-1) + P(N-5)

T = int(input())
P = {1:1, 2:1, 3:1, 4:2, 5:2}
for i in range(6, 101):
    P[i] = P[i-1] + P[i-5]
for _ in range(T):
    print(P[int(input())])