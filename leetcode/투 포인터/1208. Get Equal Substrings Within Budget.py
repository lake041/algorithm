# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
# 투 포인터

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        x = [abs(ord(u)-ord(v)) for u, v in zip(s, t)]
        
        max_len = 0
        cur_sum, left = 0, 0
        for right, num in enumerate(x):
            cur_sum += num
            while cur_sum > maxCost:
                cur_sum -= x[left]
                left += 1
            max_len = max(max_len, right-left+1)

        return max_len