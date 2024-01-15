from functools import cmp_to_key

def compare(num1, num2): # 오름차순 정렬
    ONE = int(str(num1) + str(num2))
    TWO = int(str(num2) + str(num1))
    if ONE < TWO: # 앞이 더 작다
        return -1
    elif ONE > TWO: # 앞이 더 크다
        return 1
    else:
        return 0

def solution(numbers):
    nums = [str(num) for num in numbers]
    nums.sort(key = cmp_to_key(compare), reverse = True)
    answer = ''.join(nums)

    return str(int(answer)) # "00000" => "0"