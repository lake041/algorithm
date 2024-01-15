from sys import maxsize

def cal(num, times):
    _sum = 0
    for time in times:
        _sum += num//time
    return _sum

def bisect(target, times):
    left, right = 0, maxsize
    
    while left <= right:
        mid = (left + right) // 2
        result = cal(mid, times)

        if result == target:
            right = mid - 1
        elif result > target:
            right = mid - 1
        elif result < target:
            left = mid + 1
    
    return left

def solution(n, times):
    answer = bisect(n, times)
    
    return answer