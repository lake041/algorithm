from collections import defaultdict

def solution(gems):
    N, total_unique = len(gems), len(set(gems))
    ans, cur = [0, N-1], [0, 0]
    cur_gems = defaultdict(int)
    cur_gems[gems[0]] += 1
    cur_gems_count = 1
    
    while True:
        if cur_gems_count == total_unique:
            if cur[1]-cur[0] < ans[1]-ans[0] or (cur[1]-cur[0] == ans[1]-ans[0] and cur[0] < ans[0]):
                ans = cur[:]
            cur_gems[gems[cur[0]]] -= 1
            if not cur_gems[gems[cur[0]]]:
                cur_gems_count -= 1
            cur[0] += 1
        elif cur[1] == N-1:
            break
        else:
            cur[1] += 1
            if not cur_gems[gems[cur[1]]]:
                cur_gems_count += 1
            cur_gems[gems[cur[1]]] += 1
            
    ans = [x+1 for x in ans]
    return ans