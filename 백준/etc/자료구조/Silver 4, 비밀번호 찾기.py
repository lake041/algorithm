from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
d = {}
for _ in range(N):
    URL, PW = input().split()
    d[URL] = PW
for _ in range(M):
    print(d[input().rstrip()])