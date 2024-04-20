from collections import deque

def solution(progresses, speeds):
    answer = []

    q = deque(list(map(list, zip(progresses, speeds))))

    while q:
        for i in range(len(q)):
            q[i][0] += q[i][1]

        cnt = 0    
        while True:
            if q and q[0][0] >= 100:
                q.popleft()
                cnt += 1
            else:
                break
        
        if cnt:
            answer.append(cnt)
    
    return answer