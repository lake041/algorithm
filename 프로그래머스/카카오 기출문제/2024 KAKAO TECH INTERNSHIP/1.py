from collections import defaultdict

def solution(friends, gifts):
    score = defaultdict(int)
    combi = defaultdict(int)

    for friend in friends:
        score[friend] = 0

    for record in gifts:
        giver, taker = record.split()
        combi[(giver, taker)] += 1
        score[giver] += 1
        score[taker] -= 1

    ans = -1
    for i in friends:
        temp = 0
        for j in friends:
            if i == j:
                continue
            if combi[(i, j)] > combi[(j, i)]:
                temp += 1
            if combi[(i, j)] == combi[(j, i)] and score[i] > score[j]:
                temp += 1
        ans = max(ans, temp)

    return ans