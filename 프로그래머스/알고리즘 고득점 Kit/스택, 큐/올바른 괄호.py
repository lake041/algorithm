def solution(s):
    answer = True
    stack = []
    for char in s:
        if not stack:
            if char == '(':
                stack.append(char)
            else:
                answer = False
                break
        else:
            if stack[-1] == '(' and char == ')':
                stack.pop()
            elif stack[-1] == '(' and char == '(':
                stack.append(char)
            else:
                answer = False
                break
    
    if stack:
        answer = False

    return answer