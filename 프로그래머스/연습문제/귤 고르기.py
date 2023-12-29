from collections import Counter

def solution(k, tangerine):
    # 힙스터 풀이
    # return sum(1 for _, num in Counter(tangerine).most_common() if (k:=k-num)>=0 or (k+num>0 and k<=0))

    c = Counter(tangerine)
    hap, cnt = 0, 0
    for _, num in c.most_common():
        hap += num
        cnt += 1
        if k <= hap:
            break
        
    return cnt