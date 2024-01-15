from collections import defaultdict

def solution(str1, str2):
    str1, str2 = list(str1), list(str2)
    chk1, chk2 = [False]*len(str1), [False]*len(str2)
    dic = {}

    for index, char in enumerate(str1):
        if 'A' <= char <= 'Z':
            str1[index] = char.lower()
        if 'a' <= str1[index] <= 'z':
            chk1[index] = True

    for index, char in enumerate(str2):
        if 'A' <= char <= 'Z':
            str2[index] = char.lower()
        if 'a' <= str2[index] <= 'z':
            chk2[index] = True

    for i in range(len(str1)-1):
        if chk1[i] and chk1[i+1]:
            if str1[i]+str1[i+1] not in dic:
                dic[str1[i]+str1[i+1]] = [0, 0]
            dic[str1[i]+str1[i+1]][0] += 1

    for i in range(len(str2)-1):
        if chk2[i] and chk2[i+1]:
            if str2[i]+str2[i+1] not in dic:
                dic[str2[i]+str2[i+1]] = [0, 0]
            dic[str2[i]+str2[i+1]][1] += 1

    hap, gyo = 0, 0
    for value in dic.values():
        hap += max(value)
        gyo += min(value)
    gap = int((gyo/hap)*65536) if hap != 0 else 65536
    
    return gap