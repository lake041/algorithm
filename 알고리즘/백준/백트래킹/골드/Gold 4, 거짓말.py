# https://www.acmicpc.net/problem/1043

N, M = map(int, input().split())
know_truth = list(map(int, input().split()))
know_truth = know_truth[1:] if len(know_truth) > 1 else []
party = [list(map(int, input().split()))[1:] for _ in range(M)]

ans = 0
check = [False]*M

def go(index, count, know_truth, know_lie):
    global ans
    if index == M:
        ans = max(ans, count)
        return

    # 진실을 말한 경우
    can_truth = True
    for member in party[index]:
        if member in know_lie:
            can_truth = False
    if can_truth:
        go(index+1, count, know_truth + party[index], know_lie)

    # 거짓을 말한 경우
    can_lie = True
    for member in party[index]:
        if member in know_truth:
            can_lie = False
    if can_lie:
        go(index+1, count+1, know_truth, know_lie + party[index])

go(0, 0, know_truth, [])
print(ans)