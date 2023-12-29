from collections import deque

# 더 깔끔한 풀이로 다시 풀려고 했는데 이 풀이를 유지한다.
def solution(priorities, location):
    x = []
    for i in range(len(priorities)):
        x.append(priorities[i])
        priorities[i] = (priorities[i], i)
    x.sort()
    priorities = deque(priorities)
    
    cnt = 0
    while True:
        priority, index = priorities.popleft()
        if x[-1] == priority:
            x.pop()
            cnt += 1
            if index == location:
                break
        else:
            priorities.append((priority, index))
        
    return cnt