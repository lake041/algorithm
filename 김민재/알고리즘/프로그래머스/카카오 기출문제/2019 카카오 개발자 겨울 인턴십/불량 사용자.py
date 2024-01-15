from itertools import combinations, permutations

def possible(u, b):
    return len(u)==len(b) and all(y in (x, "*") for x, y in zip(u, b))

def solution(user_id, banned_id):
    ans = 0
    for user_combi in combinations(user_id, len(banned_id)):
        for user_permu in permutations(user_combi, len(banned_id)):
            if all(possible(u, b) for u, b in zip(user_permu, banned_id)):
                ans += 1
                break
            
    return ans