def solution(nums):
    answer = 0
    dic = {}
    for num in nums:
        if num in dic:
            pass
        else:
            dic[num] = 1
    answer = min(len(nums)//2, len(dic))
    return answer