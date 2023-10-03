# MBTI 종류는 총 16가지
# 비둘기집의 원리에 의해 N>=33이라면 반드시 3개 이상이 중복되는 MBTI가 생긴다

from sys import maxsize
from itertools import combinations

def cal(str1, str2, str3):
    diff = 0
    for i in range(4):
        if str1[i] != str2[i]:
            diff += 1
        if str2[i] != str3[i]:
            diff += 1
        if str3[i] != str1[i]:
            diff += 1
    return diff

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(input().split())
    if N >= 33:
        print(0)
        continue

    minValue = maxsize
    for x, y, z in combinations(data, 3):
        minValue = min(minValue, cal(x, y, z))
    print(minValue)

'''
3
3
ENTJ INTP ESFJ
4
ESFP ESFP ESFP ESFP
5
INFP INFP ESTP ESTJ ISTJ
'''