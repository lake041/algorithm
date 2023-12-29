from collections import deque, defaultdict

def can_transit(A, B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    return True if count == 1 else False

def solution(begin, target, words):
    answer = 0
    q = deque([(begin, 0)])
    visited = defaultdict(bool)
    while q:
        now, cnt = q.popleft()
        if now == target:
            answer = cnt
            
        for word in words:
            if visited[word]:
                continue
            if can_transit(now, word):
                q.append((word, cnt+1))
                visited[word] = True

    return answer