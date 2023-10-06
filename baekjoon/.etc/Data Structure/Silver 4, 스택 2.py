from sys import stdin
input = stdin.readline

N = int(input())
stack = []
length = 0

for _ in range(N):
    order = input().rstrip().split()
    if len(order) == 2:
        stack.append(order[1])
        length += 1
    elif order[0] == '2':
        if stack:
            print(stack.pop())
            length -= 1
        else:
            print(-1)
    elif order[0] == '3':
        print(length)
    elif order[0] == '4':
        print(1 if not stack else 0)
    elif order[0] == '5':
        print(stack[-1] if stack else -1)