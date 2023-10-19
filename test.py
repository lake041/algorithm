from collections import deque, defaultdict
from itertools import combinations, permutations, product

# print(len(list(combinations(range(13), 2))))

nums = [int(input()) for _ in range(5)]
nums.sort()
print(sum(nums)//5, nums[2])