from sys import maxsize

def cal(sx, sy, tx, ty):
    return (tx-sx)**2 + (ty-sy)**2

# 대각선은 기하학적으로 최단거리가 될 수 없음
def find_shortest(sx, sy, tx, ty, m, n):
    d = []
    if not(sx==tx and sy<ty): # 북
        d.append(cal(sx, sy, tx, 2*n-ty))
    if not(sx<tx and sy==ty): # 동
        d.append(cal(sx, sy, 2*m-tx, ty))
    if not(sx==tx and sy>ty): # 남
        d.append(cal(sx, sy, tx, -ty))
    if not(sx>tx and sy==ty): # 서
        d.append(cal(sx, sy, -tx, ty))
    
    return min(d)

def solution(m, n, startX, startY, balls):
    answer = []
    for tx, ty in balls:
        answer.append(find_shortest(startX, startY, tx, ty, m, n))
    return answer