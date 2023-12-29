def solution(s):
    bin_cnt, remove_cnt = 0, 0
    while s != "1":
        bin_cnt += 1
        one_cnt = sum([1 for char in s if char == '1'])
        remove_cnt += sum([1 for char in s if char == '0']) 
        s = bin(one_cnt)[2:]
    return [bin_cnt, remove_cnt]