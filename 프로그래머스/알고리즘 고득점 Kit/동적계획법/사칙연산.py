from sys import maxsize

# 어렵다.
# ["1", "-", "10", "-", "100", "+", "1", "-", "10", "-", "100", "+", "1"]
# 1 - (10 - (100 + 1) - 10 - 100) + 1

def solution(arr):
    nums, ops = [], []
    for index, value in enumerate(arr):
        nums.append(int(value)) if index%2==0 else ops.append(value)
    
    L = len(nums)
    MAX = [[-maxsize]*L for _ in range(L)]
    MIN = [[maxsize]*L for _ in range(L)]

    for size in range(1, L+1):
        for start in range(L-size+1):
            end = start + size - 1
            
            if start == end:
                MAX[start][end] = nums[start]
                MIN[start][end] = nums[start]
                continue

            for mid in range(start, end):
                if ops[mid] == "+":
                    MAX[start][end] = max(MAX[start][end], 
                                          MAX[start][mid] + MAX[mid+1][end])
                    MIN[start][end] = min(MIN[start][end], 
                                          MIN[start][mid] + MIN[mid+1][end])
                if ops[mid] == "-":
                    MAX[start][end] = max(MAX[start][end], 
                                          MAX[start][mid] - MIN[mid+1][end])
                    MIN[start][end] = min(MIN[start][end], 
                                          MIN[start][mid] - MAX[mid+1][end])

    return MAX[0][-1]