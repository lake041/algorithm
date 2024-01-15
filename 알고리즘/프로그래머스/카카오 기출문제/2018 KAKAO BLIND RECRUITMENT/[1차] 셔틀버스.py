from collections import deque, Counter

def num_to_char(num):
    H, M = str(num//60), str(num%60)
    return H.zfill(2) + ":" + M.zfill(2)

def solution(n, t, m, timetable):
    timetable.sort()
    for i, time in enumerate(timetable):
        timetable[i] = int(time[:2])*60 + int(time[3:])
    timetable = deque(timetable)
    
    bus = deque()
    for i in range(n):
        bus.append(540 + t*i)

    while True:
        cnt = 0 # 탑승인원
        last = 0 # 마지막 탑승인원의 도착 시간
        while timetable and timetable[0] <= bus[0] and cnt < m:
            last = timetable.popleft()
            cnt += 1

        if len(bus) > 1:
            bus.popleft()
            continue

        # 마지막 버스의 자리가 남은 경우, 마지막 버스 도착 시간에 도착한다
        if cnt < m:
            return num_to_char(bus[0])
        
        # 마지막 버스의 자리가 꽉찬 경우
        if cnt == m:
            return num_to_char(last-1) if last else num_to_char(bus[0])