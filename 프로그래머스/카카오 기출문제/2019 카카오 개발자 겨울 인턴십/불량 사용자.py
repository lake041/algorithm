from itertools import combinations, permutations

def possible(id, banned):
    return len(id) == len(banned) and all(b == '*' or i == b for i, b in zip(id, banned))

def solution(user_id, banned_id):
    cnt = 0
    for combination in combinations(range(len(user_id)), len(banned_id)):
        for permu in permutations(combination, len(banned_id)):
            permu = [user_id[index] for index in permu]
            if all(possible(id, banned) for id, banned in zip(permu, banned_id)):
                cnt += 1
                break

    return cnt