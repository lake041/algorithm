from collections import defaultdict
def solution(phone_book):
    answer = True
    dic = defaultdict(int)
    for num in phone_book:
        dic[num] = 1
    for num in phone_book:
        lenNum = len(num)
        for i in range(0, lenNum-1):
            if dic[num[0:i+1]] == 1:
                return False
    return answer