from sys import maxsize

def solution(sequence, k):
    answer = [0, 0]
    min_length = maxsize
    for left in range(len(sequence)):
        for right in range(left+1, len(sequence)+1):
            if sum(sequence[left:right]) > k:
                break
            if sum(sequence[left:right]) < k:
                continue
            if sum(sequence[left:right]) == k and (right-left) < min_length:
                answer = [left, right-1]
                min_length = right - left
                break
    return answer