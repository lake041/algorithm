from sys import maxsize
from collections import deque

def solution(sequence, k):
    answer = []
    sequence += [0]

    q = deque()
    sum = 0
    left, right = 0, 0
    length = maxsize
    for i in range(len(sequence)):
        while sum > k:
            temp = q.popleft()
            sum -= temp
            left += 1
        if sum == k and right - left + 1 < length:
            answer = [left, right]
            length = right - left + 1

        q.append(sequence[i])
        sum += sequence[i]
        right = i

    return answer
