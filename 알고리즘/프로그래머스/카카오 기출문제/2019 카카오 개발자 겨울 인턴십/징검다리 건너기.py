# 1. 시간초과
'''
def solution(stones, k):
    cnt = 0
    while True:
        indexes = []
        zero_seq = 0
        done = False
        for index, number in enumerate(stones):
            if number == 0:
                zero_seq += 1
            else:
                zero_seq = 0
                indexes.append(index)
                
            if zero_seq == k:
                done = True
                break

        if done:
            break
        
        min_value = min([stones[index] for index in indexes])
        for index in indexes:
            stones[index] -= min_value
        cnt += min_value
        
    
    return cnt
'''

# 2. 시간초과
'''
def solution(stones, k):
    return min([max(stones[i:i+k]) for i in range(len(stones)-k+1)])
'''

from collections import deque

def solution(nums, k):
    mq = deque()
    maxes = []

    for i in range(len(nums)):            
        if mq and mq[0] <= i - k: mq.popleft()
        while mq and nums[mq[-1]] <= nums[i]: mq.pop()

        mq.append(i)
        if i >= k - 1: maxes.append(nums[mq[0]])
        
    return min(maxes)
