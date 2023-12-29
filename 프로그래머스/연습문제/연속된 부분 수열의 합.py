from sys import maxsize

# 직관적인 이해가 안 된다.

def solution(seq, k):
    ans = [0, 0]
    sum = 0
    right = 0
    interval = maxsize

    for left in range(len(seq)):
        while sum < k and right < len(seq):
            sum += seq[right]
            right += 1
        if sum == k and right-left+1 < interval:
            ans = [left, right-1]
            interval = right-left+1
        sum -= seq[left]
    return ans