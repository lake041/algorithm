from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for permutation in permutations(dungeons):
        fatigue = k
        cnt = 0
        for need, use in permutation:
            if fatigue >= need:
                fatigue -= use
                cnt += 1
        answer = max(answer, cnt)
        
    return answer