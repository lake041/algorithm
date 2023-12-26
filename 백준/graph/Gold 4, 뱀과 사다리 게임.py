from collections import deque

N, M = map(int, input().split())
ladder, snake = {}, {}

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

visited = [False] * 101
visited[1] = True
ans = 0
q = deque([(1, 0)])

while q:
    now, cnt = q.popleft()

    # cnt가 작은 순서대로 pop되기 때문에 다른 조건을 붙이지 않아도 된다.
    if now == 100:
        ans = cnt
        break

    # 어차피 별 차이 안 난다. 그냥 모든 경우의 수를 다 넣자.
    for i in range(1, 7):
        next = now + i
        if next <= 100 and not visited[next]:
            visited[next] = True
            if next in ladder:
                next = ladder[next]
            elif next in snake:
                next = snake[next]
            visited[next] = True

            q.append((next, cnt + 1))

print(ans)
