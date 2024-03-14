from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))
prefix = [scores[0]]
for score in scores[1:]:
    prefix.append(prefix[-1] + score)

for _ in range(K):
    start, end = map(int, input().split())
    start, end = start-1, end-1
    hap = prefix[end] - prefix[start] + scores[start]
    div = round(hap / (end - start + 1), 2)
    ans = format(div, ".2f")
    print(ans)