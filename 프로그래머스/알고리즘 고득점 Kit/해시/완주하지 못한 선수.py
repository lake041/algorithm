from collections import defaultdict
def solution(participant, completion):
    answer = ''
    d = defaultdict(int)
    for person in completion:
        d[person] += 1
    for person in participant:
        d[person] -= 1
        if d[person] < 0:
            answer = person
    return answer