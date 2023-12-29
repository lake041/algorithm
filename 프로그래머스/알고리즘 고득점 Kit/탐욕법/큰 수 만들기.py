def solution(number, k):
    number = list(number)
    
    stack = []
    cnt = 0
    for num in number:
        if not stack:
            stack.append(num)
            continue
        if stack[-1] >= num:
            stack.append(num)
        else:
            while stack and stack[-1] < num and cnt < k:
                stack.pop()
                cnt += 1
            stack.append(num)
    
    for _ in range(k-cnt):
        stack.pop()
    
    return ''.join(stack)