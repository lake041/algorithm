'''
for student in lost:
    if student in reserve:
        lost.remove(student)
        reserve.remove(student)

for element in list: 도 내부적으로는 인덱스로 접근한다.
따라서 순회를 하면서 삭제를 하면 문제가 발생한다.
'''

def solution(n, lost, reserve):
    lost.sort()
    cannot = []
    for student in lost:
        if student in reserve:
            cannot.append(student)
    
    for student in cannot:
        lost.remove(student)
        reserve.remove(student)

    cnt = n - len(lost)
    for student in lost:
        if student-1 in reserve:
            cnt += 1
            reserve.remove(student-1)
            continue
        if student+1 in reserve:
            cnt += 1
            reserve.remove(student+1)
            continue

    return cnt