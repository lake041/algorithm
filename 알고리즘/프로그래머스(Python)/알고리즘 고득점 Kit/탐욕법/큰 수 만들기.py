from collections import deque

def solution(number, k):
    number = deque(number)
    stack = []
    
    while number and k:
        if not stack:
            stack.append(number.popleft())
        elif stack[-1] >= number[0]:
            stack.append(number.popleft())
        elif stack[-1] < number[0]:
            stack.pop()
            k -= 1
    
    for _ in range(k):
        stack.pop()
    
    stack.extend(list(number))
    
    return ''.join(stack)