# 자주하는 실수
# 1. iteration을 수행할 때, 초기화 해야하는 값과 초기화 하는 위치를 정확하게 파악하자
# 2. 추가 테스트 케이스를 머리로만 생각하지 말고 직접 입력해서 확인하자
# 3. 수시로 디버깅하면서 풀이를 작성하자 

from sys import maxsize
from copy import deepcopy

def go_right(start, length):
    return 0 if start==length-1 else start+1

def go_left(start, length):
    return length-1 if start==0 else start-1

def cal(a1, a2):
    # ord(A) = 65
    # ord(Z) = 90
    x = abs(ord(a1)-ord(a2))
    y = abs(ord(a1)-ord('A')+1 + ord('Z')-ord(a2))
    return min(x, y)

def solution(name):
    answer = 0
    for alpha in name:
        answer += cal('A', alpha)
        
    L = len(name)
    name = list(name)
    name[0] = "A"
    plus = [maxsize, maxsize]
    
    if name == ["A"]*L:
        return answer
    
    # 우로 가다가 좌로 직진
    for i in range(L):
        _name = deepcopy(name)
        cur, _sum, end = 0, 0, False
        for _ in range(i):
            cur = go_right(cur, L)
            _name[cur] = "A"
            _sum += 1
            if _name == ["A"]*L:
                end = True
                break
        if not end:
            for _ in range(L):
                cur = go_left(cur, L)
                _name[cur] = "A"
                _sum += 1
                if _name == ["A"]*L:
                    break
        plus[0] = min(plus[0], _sum)
    
    # 좌로 가다가 우로 직진
    for i in range(L):
        _name = deepcopy(name)
        cur, _sum, end = 0, 0, False
        for _ in range(i):
            cur = go_left(cur, L)
            _name[cur] = "A"
            _sum += 1
            if _name == ["A"]*L:
                end = True
                break
        if not end:
            for _ in range(L):
                cur = go_right(cur, L)
                _name[cur] = "A"
                _sum += 1
                if _name == ["A"]*L:
                    break
        plus[1] = min(plus[1], _sum)
    
    return answer + min(plus)